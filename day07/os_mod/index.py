#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import os

print(os.getcwd())      # 返回当前目录

print(os.path.normpath(os.path.join(os.path.abspath(__file__),'..','..')))   # normpath 去除..之类的

os.system('ls -l')

print(os.stat('index.py'))    # 获取文件或目录信息
print(os.stat('index.py').st_size)    # 文件大小 betys

print(os.listdir(os.path.dirname(__file__)))     # listdir 列出文件夹下的所有的 子目录和文件


print(os.sep)     # 列出系统的分隔符


print(os.environ)           # 返回全局环境变量 字典
os.environ['test_name'] = 'jmz'
print(os.environ['test_name'])


print(os.path.split('/root/b/c.txt'))    # 风隔成
print(os.path.dirname(__file__))   # 返回当前文件夹或文件的 目录
print(os.path.basename('/root/b/c.txt'))
# print(os.)
