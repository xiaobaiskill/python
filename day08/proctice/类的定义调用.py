#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 1.1定义类
# 1.1.1 无参定义
class test(object):
    def __init__(self):
        pass
    def func(self):  # 类方法
        pass
# 1.1.2 有参定义
class foo(object):
    def __init__(self,name,age):
        self.name = name    # 类属性
        self.age = age

# 1.2 调用类(与函数的方式很像)
obj = test()
# obj 此刻叫对象，是实例化test类后，产生的对象
print(obj)
# <__main__.test object at 0x00000000024C7EF0>
obj1 = foo('王大炮',23)   # 调用类时传参，等于调用了类中的__init__方法，调用该方法和调用函数一样，只是在调用是会传入self自身参数
print(obj1.age)  # 对象属性调用
# 23


