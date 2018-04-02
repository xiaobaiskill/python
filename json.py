#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Auther Jmz
import json

# dict_data = {
#     'jmz':{'passwd':'123','count':0}
#     ,'qqc':{'passwd':'aaa','count':0}
#     ,'wh':{'passwd':'bbb','count':0}
# }


# 将json 存入文件中
# with open('db.txt','w',encoding='utf-8') as f:
#     json.dump(dict_data, f)


# 将json 读取出来
with open('db.txt','r',encoding='utf-8') as json_f:
    data = json.load(json_f)
    print(data['jmz']['count'])