#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz

#  1、在被装饰函数前 加上 @装饰函数
#  2、保证原有方式调用不变的情况下， 添加装饰器

# 不带参数的情况下

def test_fun(fun):
    def iner():                                 # 不理解这样的一层
        re = fun()
        return re
    return iner

@test_fun             # ====>test_fun(fun1)
def fun1():
    print('我是不带参数的')
fun1()                  # fun1() ====> test_fun(fun1)()






# 带参数的情况下

def test_fun2(fun):
    def iner2(*args,**kwargs):                  # 不理解这样的一层
        re = fun(*args,**kwargs)
        return re
    return iner2

@test_fun2       # ===> test_fun2(fun2)
def fun2(a,b):
    print('我是和平的分割线'.center(50,'-'))
    print(a)
    print(b)
    return 'lala'

fun2(b='bbb',a='aaa')               # fun2(b='bbb',a='aaa') ======> test_fun2(fun)(b='bbb',a='aaa')
print(fun2(b='bbb',a='aaa'))









# 多层装饰器
'''
@demo1
@demo2
@demo3
def foo()
    pass
foo = demo1(demo2(demo3(foo)))

'''
