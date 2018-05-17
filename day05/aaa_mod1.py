#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from aaa import bbb
# 执行顺序
#   1、先执行包文件aaa/__init__.py
#   2、后执行包文件aaa/bbb/__init__.py

print('aaa_mod1')
bbb.m_mod.fun_m_mod()





# 最后结果
#     aaa.__init__       # 先执行了aaa.__init__py
#     m1                # 在执行bbb/__init__.py 时，先导入了m_mod ,在执行m_mod.py时，
                        # 分别有导入了m1,m2 ,导入完成后执行后续代码，在执行到m1.func_m1()，调用了m1的func_m1方法
#     bbb.__init__      # 导入完后执行了print('bbb.__init__')
#     aaa_mod1
#     m_mod