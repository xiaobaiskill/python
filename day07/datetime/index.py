#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import datetime,time
print(datetime.datetime.now())
# 2018-05-21 22:52:39.542560

print(datetime.date.fromtimestamp((time.time())))
# 2018-05-21  时间转日期

print(datetime.datetime.now() + datetime.timedelta(-3))
print(datetime.datetime.now() - datetime.timedelta(3))
# 2018-05-18 22:56:21.981011  上面两个的效果是 一样的  都是 在当天的基础上减3天

print(datetime.datetime.now() + datetime.timedelta(hours=-3))
print(datetime.datetime.now() - datetime.timedelta(hours=3))
# 2018-05-21 19:58:22.163141   上面两个的效果是 一样的  都是 在当天的基础上减3小时

print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
# 2018-05-21 23:29:06.690998

c_time = datetime.datetime.now()
print(c_time.replace(minute=30,hour=2,day=19))
# 2018-05-19 02:30:19.485846