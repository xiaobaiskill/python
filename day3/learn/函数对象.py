#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz



# 函数对象：可以当成变量去处理

# 1、被赋值
def foo():
    print('from foo')
f =foo
f()

# 2、当成参数使用
def bar(func):
    print(func)

bar(foo)

# 3、当成返回值调用
def bar1(func):
    return func
bar1(foo)()

# 4、当成容器类型元素
def pull():
    print('from pull')
def push():
    print('from push')
def cat():
    print('from cat')

func_dict=[['pull',pull],['push',push],['cat',cat]]

while True:
    count = 1
    for value in func_dict:
        print(count,value[0])
        count+=1
    print('q','退出')
    chooise = input('chooise>>').strip()
    if chooise =='q':
        break
    elif int(chooise) <= len(func_dict):
        func_dict[int(chooise)-1][1]()