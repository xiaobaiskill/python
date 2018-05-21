#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import random
print(random.random())       # (0,1)  去小数
# 0.644271281361324

print(random.randint(2,4))   # [2,4]
# 4

print(random.choice([1,2,3,['a','jmz']]))     # 在[1,2,3,['a','jmz']] 中随机取一个
# 2

print(random.sample([1,2,3,['a','jmz']],2))   # [1,2,3,['a','jmz']] 中取两个 组成 新历史列表
# [3, 2]

print(random.uniform(2,5))
# 4.7414246822271595

l = ['a','d',3,4,5]
print(random.shuffle(l))   # None
print(l)                   # ['d', 'a', 3, 5, 4]
