#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import tarfile,os

# 压缩
t = tarfile.TarFile('a.tar','w')
t.add('a.txt')
t.close()

# 解压
t= tarfile.TarFile('a.tar','r')
t.extractall('./a')
t.close()




# os.remove('./a.tar')


