#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Auther Jmz
import json
#将json 存入文件中
# dict_data = {'jmz':{'passwd':'123','count':0},'qqc':{'passwd':'aaa','count':0},'wh':{'passwd':'bbb','count':0}}
# with open('json.txt', 'w', encoding='utf-8') as f:
#     json.dump(dict_data,f)


# 将json 读取出来
# 文本中json 数据一定要是双引号的  哎 ～～～   还有引入一定要注意呀
with open('json.txt', 'r', encoding='utf-8') as json_f:
    data = json.load(json_f)
    print(data['jmz'])