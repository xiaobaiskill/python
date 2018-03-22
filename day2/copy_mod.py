#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther Jmz

import copy
name = ['jmz','qqc','wh',['1','3','4']]
names1 = copy.copy(name)
names2 = copy.deepcopy(name)
name[3][1]='dsadsadsa'
names3 = copy.deepcopy(name)
print(name)
print(names1)
print(names2)
print(names3)