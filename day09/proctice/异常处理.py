#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 1、什么是异常
# 2、异常种类
# 3、什么处理异常
# 4、什么情况下使用异常处理



# 执行语法错误

# NameError
# xxx

# ValueError
# int('aaa')

# IndexError
# l=[1,2,]
# l[100]

# KeyError
# d={'x':1}
# d['y']

# TypeError
# for k in 3:  # 3 不是可迭代对象
#     print(k)

# ...



# 3\异常处理

#  3.1以下例子只能在绝对输入数字的前提下进行，否则就会报错。
# age = 23
# while True:
#     input_age = input('age>>').strip()
#     if age < int( input_age ):
#         print('too small')
#     elif age > int( input_age ):
#         print('too big')
#     else:
#         print('yes, i got')



# 3.2 异常处理代码

#  3.2.1 被动异常处理
# 用法一 ： try...except... 指定类型用法
#  try 内的代码，有错误时即会被抛出，由except 捕获，并匹配后面的错误类型，如果一致，则执行exceot 内的代码
# try:
#     xx
#     l = [1,4,2]
#     l[100]
#     d = {'x':111}
#     d['y']
# except NameError as e:
#     print('有一个nameError类型错误；%s'%e)
# print('继续执行下面的代码')


# 用法二 ： 万能报错捕获
# Exception 捕获任何类型的报错，并将异常值丢给e
# try:
#     l = [1,4,2]
#     l[4]
# except Exception as e:
#     print('错误：%s'%e)
# print('继续执行下面的代码')


# 用法三： 指定类型捕获与万能捕获 结合使用
# except 谁先捕获 就执行谁
# 下面代码中，l[4] 抛出的是InderError错误类型，与下面的except 依次匹配，在第一次就成功匹配，所以无需在向下匹配。继续执行后方代码
# try:
#     l = [1,4,2]
#     l[4]
# except IndexError as e:
#     print('这是一个IndexError错误类型：%s'%e)
# except Exception as e:
#     print('错误：%s'%e)
# print('继续执行下面的代码')

# 用法四 trt...except...else....
# else try 中代码没有报错则执行 else 内的代码程序
# else 必须跟在 try ... exceot... 的后面
# try:
#     d = {'x':1}
# except NameError as e:
#     print('这是一个NameError错误类型:%s'%e)
# except Exception as e:
#     print('这里有一个错误：%s'%e)
# else:
#     print('没有任何报错时，就可以执行我了')
#
# print('继续执行后面代码')


# 用法五 try ...finally...

# try:
#     xxx
# # except NameError as e:
# #     print('这是一个NameError错误类型:%s'%e)
# # except Exception as e:
# #     print('这里有一个错误：%s'%e)
# # else:
# #     print('没有任何报错时，就可以执行我了')
# finally:
#     print('无论是否抛出错误都执行')
# print('aahahahh')








# 3.2.2 主动异常处理
# try:
#     raise IndexError('就要这个异常')
# except IndexError as e:
#     print(e)


# 3.2.3 断言异常 assert 条件
# assert 1==2
#
# # 等同于
# if not 1==2:
#     raise AssertionError('1 != 2')




