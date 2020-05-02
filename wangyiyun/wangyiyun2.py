import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time
import requests

# 读入数据
df_comment_1 = pd.read_excel("./wangyiyun/jinglei1.xlsx")
df_comment_2 = pd.read_excel("./wangyiyun/jinglei1.xlsx")

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