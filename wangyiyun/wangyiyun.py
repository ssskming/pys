import requests
import json
import time
import pandas as pd

def parse_one_page(comment_url):
    """
    功能：给定一页的评论接口，获取一页的数据
    """
    # 添加headers
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }

    # 发起请求
    r = requests.get(comment_url,headers=headers)

    # 解析数据
    comment_data = r.json()['comments']

    # 获取用户id
    user_id = [i['user']['userId'] for i in comment_data]

    # 获取用户昵称
    nick_name = [i['user']['nickname'] for i in comment_data]

    # 获取评论ID
    comment_id = [i['commentId'] for i in comment_data]

    # 获取评论内容
    content = [i['content'] for i in comment_data]

    #获取评论时间
    content_time = [i['time'] for i in comment_data]

    # 获取点选
    liked_Count = [i['likedCount'] for i in comment_data]

    df_one = pd.DataFrame({
        'userid':user_id,
        'nick_name':nick_name,
        'comment_id':content,
        'content_time':content_time,
        'liked_Count':liked_Count
    })
    return df_one

def get_all_page(song_id):
    """
    功能：获取100页短评，目前接口一天最多获取的数据量
    """

    df_all = pd.DataFrame()

    for i in range(101):
        url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}?limit=10&offset={}'.format(song_id, i*10)

        # 调用函数
        df = parse_one_page(comment_url=url)

        #循环追加
        df_all = df_all.append(df,ignore_index=True)

        #打印进度 
        print('我正在获取第{}页的信息'.format(i + 1))

        # sleep
        time.sleep(2)
    return df_all

if __name__ == "__main__":
    song_id = '1431580747'
    df_j1 = get_all_page(song_id)
    df_j1.to_excel("jinglei1.xlsx")