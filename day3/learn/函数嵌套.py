#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz


# 函数嵌套调用

# def max2(x,y):
#     return x if x >y else y
#
# def max4(x,y,m,n):
#     res1 = max2(x,y)
#     res2 = max2(m,n)
#     return max2(res1,res2)
# print(max4(1,2,3,4))

# 函数嵌套定义
# 函数中 定义了另一个函数
# def f1():
#     print('from f1')
#     def f2():
#         print('from f2')
#         def f3():
#             print('from f3')
#         f3()
#     f2()
# f1()