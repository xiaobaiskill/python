#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import shelve

# shelve 比 pickle 更简单
f=shelve.open(r'shelve.txt',writeback=True)
# f['jmz']  ={'age':23,'weight':23.4}   # 写入文件

print(f['jmz'])


# f['jmz']['age'] =2555    # 需要开启writeback=Tru


f.close()



