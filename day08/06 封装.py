#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 封装的特性：
#   1、在类的定义阶段就已经发生类一次改变，在类的定义阶段之后，就不会在发生改变
#   2、只是一个语法上的变形，__属性变成：_类名__属性
#   3、隐藏是对内不对外的
#   4、在继承中，子类不会继承父类的私有的方法

# class Foo(object):
#     __age = '14'
#     def __f1(self,name):
#         self.__name = name
#         print('foo.__f1')
#
#     def f2(self):
#         print(self.__age)
#         self.__f1('jmz')
#         print(self.__name)
#
#
#
#
#
# obj = Foo()
# obj.f2()
# print(obj.__dict__)



# 属性封装
# class Foo(object):
#     __name = 'jmz'
#     __age = 23
#     def f2(self,name):
#         if type(name) is not str:
#             raise TypeError('name 不是字符串类型')
#         print('<%s>'%(self.__age))
#
#
#
# obj = Foo()
# obj.f2('jmz')







# 函数封装

class Foo(object):
    def __card(self):
        print('插卡')
    def __auth(self):
        print('验证')
    def without(self):
        self.__card()
        self.__auth()




