#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import hashlib,os


def echo(content):
    print('\033[1;31m %s \033[0m' % content)

def encry(pwd):
    '''
    公用加密接口
    :return:
    '''
    m=hashlib.md5()
    m.update(pwd.encode('utf-8')+b'xiaobaiskill')
    return m.hexdigest()

def getdirsize(dir):
    '''
    获取文件夹数据大小
    :param dir:
    :return:
    '''
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        print(size)
    return size





