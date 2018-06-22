#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



class foo(object):
    name = ''
    def __init__(self):
        pass
    @staticmethod      # 只需要在方法的上方加 一个 @staticmethod，同时去除 方法中的self 参数
    def func(content):
        print(content)


# 调用
obj = foo()
obj.func('我是对象非绑定方法')
# 我是对象非绑定方法
foo.func('我是类非绑定方法')
# 我是类非绑定方法


# 总结
    # 1、非绑定方法 类本省和对象都可以调用
    # 2、非绑定方法不可以直接调用类或对象本身的属性或方法


# 非绑定方法的注意点
class teacher(object):
    addr = '上海'
    def __init__(self,name,course):
        self.name = name
        self.course= course
    @staticmethod      # 只需要在方法的上方加 一个 @staticmethod，同时去除 方法中的self 参数
    def func():
        print('这里是%s'%teacher.addr)   # 这里是上海
        print('这是一位%s老师'%self.course) # 报错，因为没有self参数

teacher_li = teacher('李XX','语文')
teacher_li.func()   # 这样会

