#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz





# 1、什么是异常

# 2、如何产生异常

# 3 怎么处理异常






# 1、程序错误
# 1.1 报错顺序 执行顺序
# try....except...      except 必须在最前面
# try...else...         else 必须在except 后面
# try...finally....     必须在最后面

# try:
#     pass
# except IndexError :
#     pass
# else:
#     print('没有异常时处理')
#
# finally:
#     print('无论有没有异常都会执行')




# 1.2 报错信息


# xxx                   #NameError

# l=[1,3,'f',4]
# l[1111]                 #IndexError

# d = {'x':1}
# d['y']                   #KeyError

# 1/0                     #ZeroDivisionError





# 1.3、万能报错，不能提现出 报错类型  和 追踪信息
# try:
#     xxx
#     l = [1,2,3,3]
#     l[333]
# except Exception as e:
#     print(e)









# 2 主动报错
# raise IndexError('主动报错ßß')





# 3 自定义错误
# class MyError(BaseException):
#     def __init__(self,msg):
#         self.msg = msg
#     def __str__(self):
#         print('<%s>'%self.msg)

# raise MyError('这是自定义错误')