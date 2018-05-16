#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import simple_mod
# 导入simple_mod 模块，就是相当于 引入了 simple_mod 代码
# 用法，在使用simple_mod 的变量或函数时名，需要在变量名或函数名加上 导入的模块名（例如本次的导入的模块名simple_mod）

simple_mod.str1 = 'test1'    #重新赋值 simple_mod 中 str1 变量

print(simple_mod.str2)
# block dog

simple_mod.find()            # 调用simple_mod 中的find函数
# simple_mod:
#     str1:test1
#     str2:block dog
