#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

str1 = 'jmz'
str2 = 'block dog'
l = [1,'xx','yy','ufo',('shanghai','hefei')]

def get(index):
    '''
    获取第几个元素
    :param index:
    :return:
    '''
    global l
    if index < len(l):
        return l[int(index)-1]

def add(data):
    global l
    l.append(data)

def find():
    print('''simple_mod:
    str1:%s
    str2:%s'''%(str1,str2))

