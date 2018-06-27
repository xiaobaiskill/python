#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



'''

本质上也是互斥锁，CPython所独有的解释器锁

Cpython 在开启一个进程时会有两个线程，一个本身执行代码程序线程，还有一个是垃圾回收线程
'''