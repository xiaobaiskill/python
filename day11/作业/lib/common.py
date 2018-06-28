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

if __name__ == '__main__':
    print('\033[1;31m%s\033[0m'%'aaa')
    echo('我是进程')

