#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 列表生成式
# 语法
'''
[expression for item1 in iterable1 if condition1
for item2 in iterable2 if condition2
...
for itemN in iterableN if conditionN
]
'''
res = ['ege%s'%i for i in range(10) if i%2 ==0]
print(res,type(res))
# ['ege0', 'ege2', 'ege4', 'ege6', 'ege8'] <class 'list'>

# 类似于
res = []
for i in range(10):
    if i%2 == 0:
        res.append('ege%s'%i)
print(res)


