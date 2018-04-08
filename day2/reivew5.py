#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 集合

# | 合集
# & 交集
# - 差集
# ^ 对称差集
# ==
# 父集 >,<=
# 子集 <,<=

pythons = {'jmz','qqc','wh','jj','kk','cc'}
linuxs = {'cc','jmz','dd','aa','ff','wh'}

print(pythons | linuxs)       # 取合集
print(pythons & linuxs)       # 取交集
print(pythons - linuxs)       # 取pythons 对于 linux 的差集


