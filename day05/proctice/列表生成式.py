#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 列表生成式
# 语法 [exprocession for iterable if condition]
res = ['ege%s'%i for i in range(10) if i%2 ==0]
print(res,type(res))