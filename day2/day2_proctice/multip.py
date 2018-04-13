#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

''''''
#面向过程

# end = 9
# count = 1
# concat=''
# while count <= end :
#     start = 1
#     while start <=count:
#         concat += '''%d*%d=%d  ''' % (count, start, start * count)
#         start += 1
#     concat +='\n'
#     count += 1
# print(concat)




# 函数式编程

# 函数 正常输出99 乘法表的 list
def multiplication_table(start:int,stop:int,step:int=1):
    '''
    99乘法表 输出
    :int start:  开始
    :int stop:   结束
    :int step:  歩长
    :return list:
    '''
    count=1
    concat = []
    while count <= stop:
        w_start = start
        concat.append( '')
        while w_start<=count:
            concat[count-1] += '''%d*%d=%d  '''%(count,w_start,w_start * count)
            w_start += 1
        count += step
    return concat

# 在原函数multiplication_table， 基础上 可反转 99乘法表
def extends_multiplication_table(start:int,stop:int,step:int=1,order:str='asc'):
    order_list = multiplication_table(start,stop,step)
    if order == 'desc':
        order_list.reverse()
    return order_list


for order in extends_multiplication_table(1,9,order='desc') :
    print(order)

