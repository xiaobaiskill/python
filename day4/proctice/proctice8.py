#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


route_dic ={}
def make_route(name):
    def deco(func):
        route_dic[name] = func
        def wrapper(*args,**kwargs):
            return func(*args,**kwargs)
        return wrapper
    return deco

@make_route('func1')
def func1():
    print('func1')

@make_route('func2')
def func2():
    print('func2')


print(route_dic)