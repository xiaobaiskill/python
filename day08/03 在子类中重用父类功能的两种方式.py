#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 在子类中派生出的新方法中重用父类的功能

# 方式1、指名道姓的访问一个类的函数，与继承无关
#   OldboyPeople.__init__(self,name,age,sex)

# 方式2、super(自己的类名，self).父类的方式， 简写super().父类中的方式
# 调用super()就得到一个特殊的对象,该对象是专门用来引用父类中的方法的
# 具体的：该对象会严格的按照 MRO列表中,从当前类的父类，依次查找属性，即这种方式是严格依赖继承的
#


class a(object):
    pass

class b(a):
    pass

print(b.mro())     # c3算法 排序规则

