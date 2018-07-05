#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
def echo(content):
    print('\033[1;31m%s\033[0m'%content)

def hash_md5(data):
    import hashlib
    h = hashlib.md5()
    h.update(data.encode('utf-8'))
    return h.hexdigest()

def process(percent,width = 50,name='进度'):
    '''
    打印进度条
    :param percent: 比分比  0.24
    :param width:
    :return:
    '''
    if percent >1:
        percent = 1
    show_str = ('%%-%ds'%width)%(int(percent * width) *'#')
    print('\r%s [%s] %s%%'%(name,show_str,int(percent*100)),end='')
    
if __name__ == '__main__':
    import time
    for i in range(51):
        process(i/50)
        time.sleep(0.3)
