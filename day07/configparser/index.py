#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



import configparser

res = configparser.ConfigParser()

res.read('a.ini')

print(res.sections())
print(res.options('jmz'))


print(res.get('jmz','name'))


print(res.getint('jmz','age'))



print(res.getfloat('jmz','weight'))


print(res.getboolean('jmz','is_buteaful'))





