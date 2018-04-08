#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

#一个空格一个星星
max_level = 3
count =1

while count <=max_level:
    star=(2*count-1)*'*'
    print(star.center(max_level*2-1,' '))
    count +=1




