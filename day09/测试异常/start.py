#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os,sys
sys.path.append(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))

from test1 import src

# 在入口定义 异常处理，可以抛出所有的异常
try:
    src.run()
except Exception as e:
    print(e)



