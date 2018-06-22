#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
'''
class people(object):
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


me = people('jmz',1.75,68)
# 将方法封装成属性
print(me.bmi)    # 22.20408163265306
print(me.bmi())  # 报typeError 的错
'''

class good():
    def __init__(self,name,price):
        self.name = name
        self.__price = price # 双下线是类私有属性，只能类内部本身使用，外部无法访问
    @property
    def price(self):
        return self.__price
    @price.setter     # 改
    def price(self,price):
        is_int_price = str(price).strip().replace('.','')    # 转化成数字
        if not is_int_price.isdigit():
            raise TypeError('%s 不是数字类型'%price)
        self.__price = price
    @price.deleter   # 删
    def price(self):
        # del self.__price
        print('不让删啊老铁')

sy = good('山芋','1.3')
print(sy.price)
sy.price = 1.4
print(sy.price)
del sy.price