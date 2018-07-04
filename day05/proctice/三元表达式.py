#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
'''
语法：
   成立1 if condition1 else 成立2 if condition2 else ... if 成立N conditionN else 不成立
'''


sex = 'man'
print('正确' if sex == 'man' else '错误')
# 正确
'''
语句解析：
sex = 'man'
if sex == 'man':
    print('正确')
else:
    print('错误')
'''

age = 23
res = '猜大了' if age > 23 else '猜小了' if age < 23 else '猜对了'
print(res)
# '猜对了'
'''
语句解析：
age = 23
if age >23:
    res = '猜大了'
elif age <23:
    res = '猜小了'
else:
    res = '猜对了'
'''