#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 1、定义基类，子类实现基类的方法
# import abc
# class animal(metaclass=abc.ABCMeta):
#     def talk(self):
#         pass
#
# class pig(animal):
#     def talk(self):
#         print('哼哼哼')
#
# class dog(animal):
#     def talk(self):
#         print('汪汪汪')
#
# class people(animal):
#     def talk(self):
#         print('hello world')
#
# pig = pig()
# dog = dog()
# people = people()
#
# pig.talk()
# dog.talk()
# people.talk()


# 2、
class pig(animal):
    def talk(self):
        print('哼哼哼')

class dog(animal):
    def talk(self):
        print('汪汪汪')

class people(animal):
    def talk(self):
        print('hello world')


pig = pig()
dog = dog()
people = people()

pig.talk()
dog.talk()
people.talk()


