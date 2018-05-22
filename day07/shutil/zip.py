#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import zipfile

# zip 压缩
z = zipfile.ZipFile('a.zip','w')
z.write('a.txt')
z.write('index.py')
z.close()


# zip解压
z = zipfile.ZipFile('a.zip','r')
z.extractall('./a')
z.close()



