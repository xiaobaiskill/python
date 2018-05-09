#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 什么是迭代器

# 为什么需要使用迭代器

# 怎么使用迭代器
#     可迭代对象：在python中但凡有内置方法__iter__的对象，都是可迭代对象
#     迭代器对象 ：
#         执行可迭代对象下__iter__方法后得到迭代器对象
#     迭代器对象的内置方法
#         __next__
#         __iter__方法,执行该方法得到仍然是迭代器本身，干什么用？？

#       注意：
#             1、迭代器对象一定是对迭代对象
            # 2、可迭代对象不一定是迭代器对象


# 总结：
# 优点：
#     提供了一种不依赖与索引的取值方式---> 运用for循环
#     节省内存

# print(range(1,2000000))
# python2 和 python3 中着




a = 1
b = 1.1
# 以下都是可以使用__iter__ 方法
c = 'abcd'
#c.__iter__()
d = ['a','b','c']
# d.__iter__()
e = ('a','b','c')
# e.__iter__()
f = {'a':1,'b':2}
# f.__iter__()
g={'a','b','c'}
# g.__iter__()
# h=open('a.txt','r')  # 本身就是一个迭代器对象


#for循环的底层运行机制：for循环可以称之为迭代器循环
#1、先调用in后那个对象的__iter__方法，得到该对象的迭代器对象
#2、执行迭代器对象的__next__方法，将得到的返回值赋值in前面的变量名，然后执行一次循环体代码
#3、循环往复，直到取干净迭代器内所有的值，自动捕捉异常结束循环
dic = {'a':1,'b':2}

iter_obj = dic.__iter__()
while True:
    try :
        print(dic[iter_obj.__next__()])
    except StopIteration:
        break

for k in dic: #iter_obj=dic.__iter__()
    print(dic[k])

# # 索引的迭代方式
# # 列表是自带索引的，那么如何迭代没有索引的呢？？？（禁止使用for）
# l = ['a','b','c']
# k = 0
# while k<len(l):
#     print(l[k])
#     k+=1



# #  __iter__方法,执行该方法得到仍然是迭代器本身
# dic = {'a':1,'b':2,'c':3,'d':4}
# iter_obj = dic.__iter__()
# print(next(iter_obj))     # a
# print(next(iter_obj))     # b
#
# iter_obj1 = dic.__iter__()      # 重写开始了一个新的迭代器 对象
# print(next(iter_obj1))    # a
#
#
# iter_obj = iter_obj.__iter__()      # iter_obj.__iter__()  is iter_obj     #True
# print(next(iter_obj))     # c
# print(next(iter_obj))     # d




