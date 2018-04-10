#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


#  非固定参数 kwargs
# 注意事项：
#   1、 多余的关键参数会被保存到 kwargs中作为字典保存
#   2、 位置参数必须在前
#   3、 位置参数可以已关键参数表示，多余的关键参数会被放入kwargs 中
#   4、 多余的位置参数无法保存在 kwargs 中。

def person(you,she,**kwargs):
    print(you,she)
    print(type(kwargs))
    print(kwargs)



person('xioabaiskil','jly',he='wh',girl='nv')


person(she='lala',you='jmz',he='wh111',girl='nv1111')



