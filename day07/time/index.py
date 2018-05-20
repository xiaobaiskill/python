#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import time

# 1、时间戳
print(time.time())      # 带毫秒的


# 2、格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))




# 3、结构化时间

print(time.localtime())      # 本地东八区时间
print(time.gmtime())        # 世界时间





# 时间戳 结构时间 互转
print(time.localtime(1526695858.4697459))
print(time.gmtime(1526695858.4697459))

print(time.mktime(time.localtime()))


# 结构时间 与 格式化时间互转
print(time.strftime('%Y-%M-%d',time.localtime()))

print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))





import datetime






