#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz
# global nonlocal 关键字

# test = 'this is global test'


# global
test = 'this is global test'
def test1():
    global test              #  先定义test 变量为全局变量,在函数内部再此之前不能有
    test = 'this is hahaha '
    return test
print(test1())


# nonlocal
count = 2
def test2():
    count = 1
    def test3():
        nonlocal count                  # 使用外层的变量而非全局
        return count
    return test3
print(test2()())


#nonlocal
name = 'jmz'
def test4():
    name = 'jly'
    def test5():
        def test6():
            nonlocal name                 # 一直会找到外层的 变量，而非全局变量
            return name
        return test6
    return test5
print(test4()()())



# global and nonlocal
count = 1
def test_type():
    def test_local():
        count=3
        return count
    def test_nonlocal():
        nonlocal count                 # 这是取的外一层的 count =2
        count+=10
        return count
    def test_global():
        global count                   # 这是取的全部的count=1
        count +=200
        return count
    count =2
    print('test_local of %d'% test_local())
    print('test_nonlocal of %d' % test_nonlocal())
    print('test_global of %d' % test_global())

test_type()