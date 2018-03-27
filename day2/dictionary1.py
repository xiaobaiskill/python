#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther Jmz

info = {
    "安徽":{
        "滁州":["天长","明光"]
        ,"合肥":["肥东","肥西","合肥市"]
        ,"阜阳":["阜南","界首","临泉","太和","颖上"]
    }
    ,"上海":{
        "上海市":['浦东新区',"青浦区"]
    }
    ,"广州":{
        "潮州":["潮安市","饶平"]
        ,"东莞":["东莞"]
        ,"佛山":["佛山市"]
        ,"河源":["东源","河源市","连平","龙川","紫金"],
    }
}

info['安徽']['滁州'].append('来安')
info['安徽']['滁州'][1] = "全椒"

print('setdefault 存在不添加，不存在创建'.center(50,'-'))
info.setdefault('台湾',{"台南":["台南市","lala"]})                   # 不存在则添加

print(info)

info.setdefault('上海',{"上海市":["静安区","徐汇区"]})                # 存在则不添加
print(info)
print('update'.center(50,'-'))
b={
    "江苏":{
        "南京市":['雨花台区','六合区']
    }
    ,"广州":{
        "潮州":["潮安市"]
    }
    ,"台湾":{
        "台南":["台南市"]
    }
}
info.update(b)                                                      # 有则覆盖，没有创建
print(info)
print('字典转列表'.center(50,'-'))
print(info.items())                                                 # 字典转列表
print('浅copy'.center(50,'-'))
c = info.fromkeys([6,7,8],[1,{"name":"jmz"},444])           # dict.formkeys([6,7,8],'dsadda')
c[7][1]["name"] = "dsada"                                   # 其实是浅copy
print(c)

print('循环'.center(50,'-'))

for i in info:
    print(i,info[i])
print('----上面比下面高效---')
for k,v in info.items():
    print(k,v)