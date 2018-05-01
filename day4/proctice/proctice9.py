#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import time

def logger(file):
    def deco(func):
        def wrapper(*args,**kwargs):
            with open(file,'a',encoding='utf-8') as f:
                f.write('%s %s run\n' %(time.strftime('%Y-%m-%d %X'),func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return deco

@logger('a.log')
def func1():
    return 'func1'

print(func1())