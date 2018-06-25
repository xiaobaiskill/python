#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



class test():
    def __init__(self,*args):
        self.l = args
    def index(self):
        pass



a = test(*['a','b',1,3,4])

print(a.l)