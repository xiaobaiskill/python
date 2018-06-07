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

def process_bar(percent,width=50):
    format = ('%%-%ss'%width)%(int(percent*width)*'#')
    print('\r[%s] %s%%'%(format,int(percent*100)),end='')


if __name__ == '__main__':
    import time

    start_size = 0
    total_size = 1239400
    while start_size < total_size:
        start_size+=1023
        process_bar(start_size/total_size,50)
        time.sleep(0.01)



