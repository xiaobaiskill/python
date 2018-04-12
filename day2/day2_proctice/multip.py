#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz




'''
#面向过程
end = 9
count = 1
while count <= end :
    start = 1
    while start <=count:
        print(count, '*', start, '=', start * count, end='  ')
        start += 1

    count += 1
    print()

'''


# 函数式编程
def multiplication_table(start,stop,step=1,order='asc'):
    '''
    :int start:  初始值
    :int stop:   结束值
    :int step:   步长    默认为1
    :str order:  排序方式 默认正序
    :return:     99乘法表
    '''
    count=1
    while count <= stop:
        w_start = start
        while w_start<=count:
            print(count,'*',w_start,'=',w_start * count,end='  ')
            w_start+=1
        print('')
        count +=step

multiplication_table(1,9,2)


