#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 去重操作
str = 'hello jmz say do hello jmz say say hello'
str_list=str.split();
print(type(str_list))
data = set(str_list)
print(data)
print(type(data))

print()
#--------------测试 list dict------
print('测试'.center(50,'-'))
names = ['jmz','jmz','jmz','hello','world','dsada']
str_name = "jmz jmz jmz hello world dsada"

print(set(names))   # 只能是一维的才可以 去重
print(set(str_name.split()))



