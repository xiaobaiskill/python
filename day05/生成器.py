#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 一、什么是生成器
# 函数内部含有yield关键字，那么该函数（） 即为生成器。
# 自定义迭代器

# def func():
#     print('first')
#     yield 1
#     print('second')
#     yield 2
#     print('third')
#     yield 3
#
# f = func()
# print(f)





# 二、生成器的使用方式
# 2.1生成器使用方式一
# yield 返回值
# 生成器就是迭代器，所以用法与迭代器一样

# # 仿range函数
# def range(start:int,end:int,step=1):
#     while start < end:
#         yield start        # 当一次next 执行到这里时便会返回start,并停止，下一次操作会从本次停止的地方继续往下执行，
#         start += step       # 直到再次遇到 yield 再停止，返回后面的值
#
# num = range(1,6,2)
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())
#
# # yield ： 具有停止本次操作，并return yield 后面的值，与return的返回值一样


# 2.2生成器使用方式二
# # yield 传值操作
# def doing(name):
#     print('%s开始干活了'%name)
#     thing_list = set()
#     while True:
#         do_thing = yield thing_list          # 返回thing_list
#         print('%s 正在%s'%(name,do_thing))
#         thing_list.add(do_thing)
#
#
# xiaoming = doing('xiaoming')
# next(xiaoming)                   # 第一次使用，需暂停到yield 那边
# print(xiaoming.send('做饭'))    # 先给yield 传值， 之后再接受执行到下一个yield的返回值
# print(xiaoming.send('吃饭'))
# print(xiaoming.send('干活'))
# print(xiaoming.send('睡觉'))
# xiaoming.close()                 # 关闭生成器
# xiaoming.send('起床时')         # 此时无法再传值执行，并且报错


# 总结
# 1、可以像return 一样，返回值，但又可以多次返回
# 2、可以挂起/保存函数的当前状态，可以达到随用随启动的程度
# 3、可以多次传值操作






# 作业

# 写一个取基数的操作
# def jishu():
#     num = 1
#     while True:
#         is_true = True
#         if num > 1:
#             count = 2
#             while count < num - 1:
#                 if num%count==0:
#                     is_true = False
#                     break
#                 count +=1
#         if is_true:
#             yield num
#         num +=1
#
# num = jishu()
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))


# 咖啡3元，糖0.5元 牛奶2元，平时咖啡单点的，活动需要，需加糖与牛奶捆绑销售

# def sugar(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         res += 0.5
#         return res
#     return wrapper
#
# def milk(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         res += 2.5
#         return res
#     return wrapper
#
# @sugar
# @milk
# def coffee():
#     return 3
#
#
# print(coffee())



# 用户购买商品，以邮箱或短信的形式通知
#
# def notice(type='email'):
#     def shopping(func):
#         def wrapper(*args,**kwargs):
#             if type == 'email':
#                 print('邮箱通知成功')
#             elif type == 'sms':
#                 print('短信通知成功')
#             return func(*args,**kwargs)
#         return wrapper
#     return shopping
#
#
# @notice('sms')
# def shopping(good):
#     print('成功购买了%s商品'%good)
#
# shopping('电脑')








#
