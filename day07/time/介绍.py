#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import time

# 时间戳 以unix元年（1970-01-01 00:00:00）开始计算一直到当前时间的秒数
print(time.time())
# 1526911211.354357


# 结构化时间
print(time.localtime())  # 本地的结构化时间
# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=21, tm_hour=22, tm_min=0, tm_sec=11, tm_wday=0, tm_yday=141, tm_isdst=0)
print(time.localtime().tm_year)
# 2018
print(time.gmtime())     # 世界的结构化时间
# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=21, tm_hour=14, tm_min=0, tm_sec=11, tm_wday=0, tm_yday=141, tm_isdst=0)


# 格式化时间
print(time.strftime('%Y-%m-%d %X'))
# 2018-05-21 22:00:11


# 1、时间戳  结构化时间  相互转化
print(time.localtime(1526911211.354357))     # 时间戳转结构化时间
# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=21, tm_hour=22, tm_min=0, tm_sec=11, tm_wday=0, tm_yday=141, tm_isdst=0)

print(time.mktime((2009, 2, 17, 17, 3, 38, 1, 48, 0)))    # 格式化时间转 时间戳
# 1234861418.0

# 2、结构化时间 格式化时间 相互转化
print(time.strftime('%Y-%m-%d %X',(2009, 2, 17, 17, 3, 38, 1, 48, 0)))  # 结构化时间转 格式化时间
# 2009-02-17 17:03:38
print(time.strptime('2018-04-09 14:23:14','%Y-%m-%d %H:%M:%S'))   # 格式化时间转 结构化时间

# 1.1   时间戳转结构化时间  ===> localtime,gmtime
# 1.2   结构化时间转时间戳  ===> mktime

# 2.1   结构化时间转格式化时间 ===> strftime
# 2.2   格式化时间转结构化时间 ===> strptime

