#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import shelve


# 添加数据
f= shelve.open(r'test')
f['jmz'] = {'name':'jmz','age':25,'weight':175.3}
f['jly'] = {'name':'jly','age':27,'weight':165.3}
f.close()


# 读和改
f= shelve.open(r'test',writeback=True)         # 改变数据必须要加writeback=True，添加则不需要
f['jmz']['age'] =35    # 改数据
print(f['jmz'])
f.close()

