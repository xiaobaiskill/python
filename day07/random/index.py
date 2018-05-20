#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import random
print(random.random())       # (0,1)

print(random.randint(2,4))   # [2,4]

print(random.choice([1,2,3,['a','jmz']]))     # 在[1,2,3,['a','jmz']] 中随机取一个


print(random.sample([1,2,3,['a','jmz']],2))   # [1,2,3,['a','jmz']] 中取两个 组成 新历史列表



l = ['a','d',3,4,5]
print(random.shuffle(l))
print(l)
