#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



class a:
    test = 'jmz'
    def __init__(self,age,sex):
        self.age = age
        self.sex = sex

    def find(self):
        # super().test
        print(self.test)



b = a('24','man')
print(b.__class__)

b.test = 'lll'

c = a('25','girl')


b.find()   # ==a.find(b)
c.find()

