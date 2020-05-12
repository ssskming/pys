import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time
import requests

# 读入数据
df_comment_1 = pd.read_excel("./wangyiyun/jinglei1.xlsx")
df_comment_2 = pd.read_excel("./wangyiyun/jinglei2.xlsx")

# 数据合并
df_comment = pd.concat([df_comment_1,df_comment_2])

# 去除重复值
df_comment.drop_duplicates(inplace=True)
print(df_comment.info())

# 处理时间
def timeStamp(timeNum):
    '''功能：转换毫秒为标准时间'''
    timeStamp = float(timeNum/1000) # 转换为秒
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
    return otherStyleTime

df_comment['content_time'] = df_comment['content_time'].apply(lambda x:timeStamp(x))
print(df_comment.info())

ak = ''
sk = ''
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(ak, sk)

# 请求
r = requests.post(host)

token = r.json()['access_token']

def get_sentiment(text):
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={}'.format(token)
    data = {
        'text':text
    }
    data = json.dumps(data)
    try:
        res = requests.post(url,data=data,timeout=3)
        items_score = res.json()['items']
    except Exception as e:
        time.sleep(1)
        res = requests.post(url,data=data,timeout=3)
        items_score = res.json()['items']
    return items_score

score_list = []

step = 0
for i in df_comment['content']:
    score = get_sentiment(i)
    step += 1
    print('第{}个'.format(step),end='\r')
    score_list.append(score)

# 提取正负概率
positive_prob = [i[0]['positive_prob'] for i in score_list]
negative_prob = [i[0]['negative_prob'] for i in score_list]

# 增加列
df_comment['positive_prob'] = positive_prob
df_comment['negative_prob'] = negative_prob

# 添加正向1 负向-1标签
df_comment['score_label'] = df_comment['positive_prob'].apply(lambda x:1 if x>0.5 else -1) 
df_comment.head() 

df_comment['content_time'] = pd.to_datetime(df_comment['content_time'])
df_comment['content_hour'] = df_comment.content_time.dt.hour
hour_num = df_comment.content_hour.value_counts().sort_index()

# 折线图
from pyecharts.charts import Line
from pyecharts import options as opts 

line1 = Line(init_opts=opts.InitOpts(width='1350px', height='750px'))
line1.add_xaxis(hour_num.index.tolist())
line1.add_yaxis('热度', hour_num.values.tolist(),
                label_opts=opts.LabelOpts(is_show=False))
line1.set_global_opts(title_opts=opts.TitleOpts(title='评论数时间(按小时)分布'),
                      visualmap_opts=opts.VisualMapOpts(max_=80))
line1.set_series_opts(linestyle_opts=opts.LineStyleOpts(width=3)) 
line1.render() 

# 计算占比
gender_perc = df_user['gender'].value_counts()  / df_user['gender'].value_counts() .sum()
gender_perc = np.round(gender_perc*100,2)

from pyecharts.charts import Pie

# 绘制饼图
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
pie1.add("",
         [*zip(gender_perc.index, gender_perc.values)],
         radius=["40%","65%"])
pie1.set_global_opts(title_opts=opts.TitleOpts(title='评论用户性别分布'),
                     legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
                     toolbox_opts=opts.ToolboxOpts()) 
pie1.set_series_opts(label_opts=opts.LabelOpts(formatter="{c}%"))
pie1.set_colors(['#D7655A', '#FFAF34', '#3B7BA9', '#EF9050', '#6FB27C'])
pie1.render() 

age_num = pd.Series(df_user.age.value_counts())
# 删除异常值
age_num = age_num.drop(['未知',-5, -9, 0, 1, 6, 7]) 
age_num = pd.DataFrame(age_num).reset_index().rename({'index':'age', 'age':'num'}, axis=1)

# 分箱
age_num['age_cut'] = pd.cut(age_num.age, bins=[10,15,20,25,30,35]) 

# 分组汇总
age_cut_num = age_num.groupby('age_cut')['num'].sum()


from pyecharts.charts import Bar

# 绘制柱形图
bar1 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar1.add_xaxis(age_cut_num.index.astype('str').tolist())
bar1.add_yaxis("数量", age_cut_num.values.tolist(), category_gap='20%')
bar1.set_global_opts(title_opts=opts.TitleOpts(title="评论用户年龄分布"),
                     visualmap_opts=opts.VisualMapOpts(max_=180),
                     toolbox_opts=opts.ToolboxOpts())
bar1.render()

province_num = df_user.province_name.value_counts()
province_num.index = province_num.index.str[:2]
province_top10 = province_num[:10]

# 柱形图
bar2 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar2.add_xaxis(province_top10.index.tolist())
bar2.add_yaxis("城市", province_top10.values.tolist())
bar2.set_global_opts(title_opts=opts.TitleOpts(title="评论者Top10城市分布"),
                     visualmap_opts=opts.VisualMapOpts(max_=120),
                     toolbox_opts=opts.ToolboxOpts())
bar2.render()

from pyecharts.charts import Geo
from pyecharts.globals import ChartType

# 地图
geo1 = Geo(init_opts=opts.InitOpts(width='1350px', height='750px'))
geo1.add_schema(maptype='china')
geo1.add("", [list(z) for z in zip(province_num.index.tolist(), province_num.values.tolist())], 
         type_=ChartType.EFFECT_SCATTER,
         blur_size=15) 
geo1.set_global_opts(title_opts=opts.TitleOpts(title='评论者国内城市分布'), 
                     visualmap_opts=opts.VisualMapOpts(max_=120))
geo1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo1.render()  
# 地图
map1 = Map(init_opts=opts.InitOpts(width='1350px', height='750px')) 
map1.add("", [list(z) for z in zip(province_num.index.tolist(), province_num.values.tolist())],
         maptype='china')
map1.set_global_opts(title_opts=opts.TitleOpts(title='评论者国内城市分布'),
                     visualmap_opts=opts.VisualMapOpts(max_=120),
                     toolbox_opts=opts.ToolboxOpts())
map1.render() 
label_num = df_comment.score_label.value_counts() / df_comment.score_label.value_counts().sum()
label_perc = np.round(label_num,3) 
label_perc.index = ['负向', '正向'] 
label_perc
# 绘制饼图
pie2 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
pie2.add("",
         [*zip(label_perc.index, label_perc.values)],
         radius=["40%","65%"])
pie2.set_global_opts(title_opts=opts.TitleOpts(title='评论情感标签正负向分布'),
                     legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
                     toolbox_opts=opts.ToolboxOpts()) 
pie2.set_series_opts(label_opts=opts.LabelOpts(formatter="{c}%"))
pie2.set_colors(['#3B7BA9', '#EF9050'])
pie2.render() 
# 定义分隔区间
bins = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5,
       0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
positive_num = pd.cut(df_comment.positive_prob, bins).value_counts()
positive_num = positive_num.sort_index()
# 柱形图
bar3 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar3.add_xaxis(positive_num.index.astype('str').tolist())
bar3.add_yaxis("", positive_num.values.tolist(), category_gap='5%')
bar3.set_global_opts(title_opts=opts.TitleOpts(title="评论情感得分"), 
                     visualmap_opts=opts.VisualMapOpts(max_=500),
                     toolbox_opts=opts.ToolboxOpts()
                    )
bar3.render() 
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

word1 = WordCloud(init_opts=opts.InitOpts(width='1350px', height='750px'))
word1.add("", [*zip(key_words.words, key_words.num)],
          word_size_range=[20, 200],
          shape=SymbolType.DIAMOND)
word1.set_global_opts(title_opts=opts.TitleOpts('网易云音乐关于惊雷评论词云'),
                      toolbox_opts=opts.ToolboxOpts(),
                     )
word1.render() 