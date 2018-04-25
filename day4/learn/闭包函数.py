#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz


# 什么是闭包函数：
#     1、定义在函数内的函数
#     2、该函数体代码包含对该函数外层作用域中的名字的引用，
#         强调：函数外层指的不是全局作用域
#     满足上面两个条件，那么该内部函数就称之为闭包函数。

# x=9999
# def outter():
#     x= 1
#     def input():
#         print(x)
#     return input
# f=outter() # f = input
# f()      # x=1 名字的查找关系在定义阶段就已经确定了。print(x) 现在input 中寻找，然后再在outter中寻找，最后在全局寻找,
#          # 全局查找在 调用之前寻找
# def foo():
#     x=222222
#     print('from foo')
#     f()
# foo()   # x=1




# 函数体传值的两种方式
#
# 1、参数的形式为函数体传值
# 2、以变量的形式传值
#
# def echo(x):
#     print(x)
# echo('jmz')
#
#
# y = 990
# def get_y():
#     print(y)
# get_y()





# 3、闭包函数，两种方式的结合
# def echo():
#     print('from echo')
#
# def outter(x):
#     def echo():
#         print(x)
#     return echo
#
# echo = outter(333)   # 将outter 内置函数echo 赋值给 echo，此时的echo 就是 就是内置函数echo,非全局函数echo
# echo()





# 4、闭包函数的运用
# def outter(type):
#     def get(num1,num2):
#         if type=='+':
#             print(num1+num2)
#         elif type == '*':
#             print(num1*num2)
#         else:
#             print('不合法')
#     return get
#
# jiafa = outter('+')
# jiafa(1,2)
# jiafa(3,4)
#
# chengfa=outter('*')
# chengfa(2,3)
# chengfa(4,5)

# 如果后续还需要使用加法运算 你任然可以使用 jiafa 如果想要使用乘法 你也可以使用chengfa
# 这样区分不会乱，又可随时调用





