#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz




# 要求一: 专门打印 一个 'ok'

# def fun1():
#     '''只是说明'''
#     print('ok')
# fun1()
# print(fun1.__doc__)
# print(fun1.__name__)






# 要求二 、 在原有的基础上添加函数调用前后的开始和结束标志
'''
def fun1():
    print('ok')

def fun2():
    print('start'.center(50,'-'))
    fun1()
    print('end'.center(50, '-'))
fun2()
'''
# 问题 ，如果这样的话，原来的代码调用fun1() 都要改成调用 fun2() 了






# 要求三 如何在不改变 调用方式的前提下，满足上面的要求
'''
def test_fun(fun):
    def iner():
        print('start'.center(50, '-'))
        fun()
        print('end'.center(50, '-'))
    return iner

@test_fun
def fun1():
    print('ok')
fun1()
'''






# 要求四  现在fun1  需要转递参数 打印参数，同时又要满足上面的要求该如何？
'''
def test_fun(fun):
    def iner(*args):
        print('start'.center(50, '-'))
        fun(*args)
        print('end'.center(50, '-'))
    return iner

@test_fun
def fun1(a):
    print(a)
fun1('lalala')
'''







# 要求五、 传递参数，并返回传递参数的字节数

# def test_fun(fun):
#     def iner(*args,**kwargs):
#         print('start'.center(50, '-'))
#         re = fun(*args,**kwargs)
#         print('end'.center(50, '-'))
#         return re
#     return iner
#
# @test_fun
# def fun(a):
#     ''' 这个只是打印返回字节数 '''
#     print(a)
#     return len(a)
#
# print(fun('jmz'))
# print(fun.__doc__)          # 查看函数注释
# print(fun.__name__)         # 查看函数名







# 要求六 上面的方式无法正常打印出被装饰函数的注释 和函数名，那该怎么办呢？
# 只需要 引用 from functools import wraps  并在装饰器内 添加@wraps(fun)   即可

from functools import wraps
def test_fun(fun):
    @wraps(fun)
    def iner(*args,**kwargs):
        print('start'.center(50, '-'))
        re = fun(*args,**kwargs)
        print('end'.center(50, '-'))
        return re
    return iner

@test_fun
def fun(a):
    ''' 这个只是打印返回字节数 '''
    print(a)
    return len(a)

print(fun('jmz'))
print(fun.__doc__)          # 查看函数注释
print(fun.__name__)         # 查看函数名












