#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther Jmz

person = ['jmz','qqc',['aa','bb','cc']]
p1 = person[:]                         # 浅copy 的另一种形式
p2 = person[:]

person[0] = 'jjj'
person[2][0] = 'aaa222'

print(p1)
print(p2)