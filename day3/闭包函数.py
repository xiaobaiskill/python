#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Auther Jmz

# 闭包函数
x=1
def f1():
    def f2():
        print(x)
    return f2
x=100
def f3(func):
    x=2
    func()
x=10000
f3(f1())

# 先执f1(),返回f2函数，执行F3在执行实参函数