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
    ,"江苏":{
        "南京市":['雨花台区','六合区']
    }
}

choose_flag =False
while not choose_flag:
    for i in info :
        print(i)
    choose1 = input('第一级地名：')
    if choose1 in info :
        while not choose_flag:
            for j in info[choose1] :
                print(j)
            choose2 = input('第二级地名：')
            if choose2 in info[choose1]:
                while not choose_flag:
                    for m in info[choose1][choose2] :
                        print(m)
                    choose3 = input('第三级地名：')
                    if choose3 in info[choose1][choose2]:
                        pass
                    elif choose3 == 'b':
                        break
                    elif choose3 == 'q' :
                        choose_flag = True
            elif choose2 == 'b' :
                break
            elif choose2 == 'q':
                choose_flag = True
    elif choose2 == 'b':
        break
    elif choose2 == 'q':
        choose_flag = True
