#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz




# 函数 伪装成 属性

# class people(object):
#     def __init__(self,name,weight,height):
#         self.__name = name
#         self.__height = height
#         self.__weight = weight
#     @property
#     def bmi(self):
#         return self.__weight /(self.__height**2)
#
#
# people = people('jmz',67,1.75)
# print(people.bmi)




#


class people(object):
    def __init__(self,name):
        self.__name = name

    @property   # 方法装饰成属性
    def name(self):
        return self.__name

    @name.setter    # 修改装饰方法
    def name(self,val):
        if type(val) is not str:
            raise TypeError('名字必须是字符串类型')
        self.__name = val

    @name.deleter
    def name(self):
        del self.__name



people = people('jmz')
# print(people.name())
print(people.name)
people.name = 'mmm'
print(people.name)

del people.name

# print(people.name)