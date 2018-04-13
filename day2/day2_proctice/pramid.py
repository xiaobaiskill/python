#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

#一个空格一个星星



'''
# 面向过程编程
max_level = 4
count =0

tag = True
while tag:
    num = 2 * max_level - 1
    star=(2*count+1)*'*'
    print(star.center(num,' '))
    count +=1
    if count >= max_level:
        tag=False
'''



# 函数式编程
def order_star(max_level:int,order='asc'):
    '''
    排序金字塔
    :int max_level:
    :str order:
    : 打印出金字塔
    '''
    count = 0
    tag = True
    while tag:
        num = 2 * max_level - 1
        if order =='desc':
            star = (num - count * 2) * '*'
            print(star.center(num, ' '))
        else:
            star = (2 * count + 1) * '*'
            print(star.center(num, ' '))
        count += 1

        if (order =='desc' and count > max_level) or count >= max_level:
            tag = False



order_star(4,'desc')

