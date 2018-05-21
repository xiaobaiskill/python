#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import time

# 格式化时间转 时间戳
def mktime(string,format):
    return time.mktime(time.strptime(string,format))

# 时间戳转 格式化时间
def date(format,strtime=time.time()):
    struct_time = time.localtime(strtime)
    return time.strftime(format,struct_time)

print(mktime('2017-08-09 14:13:34','%Y-%m-%d %H:%M:%S'))
# 1502259214.0


print(date('%Y-%m-%d'))
# 2018-05-21