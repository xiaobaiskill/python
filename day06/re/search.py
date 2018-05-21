#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import re

a = '23dasd2321dasdf3'

# search().group() 只取都第一个
print(re.search('\d',a).group())
# 2

#单纯使用search 可以确认是否存在值,存在为真 不存在为假
if re.search('\d',a):
    print('ok')
else:
    print('no')
# ok




