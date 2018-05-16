#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from simple_mod import *
# 导入 simple_mod 中的所有的代码
# 在当前模块空间 创建simple_mod 的变量名函数名（+引入地址）


print(str1)
# jmz

str1 = 'aaa'     # 当前模块 创建了一个变量名，以及内存地址
str2 = 'bbb'

find()        # 当前模块没有 定义函数 则调用simple_mod的函数，函数内的变量（或函数）皆使用simple_mod模块的变量（或函数）
# simple_mod:
#     str1:jmz
#     str2:block dog