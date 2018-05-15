#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz




import re


a = 'sda123dsa432'


# 已什么作为分割点，分割，  1 别是分割1次
res = re.split('\d',a,1)

print(res)