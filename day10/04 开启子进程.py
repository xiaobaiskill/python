#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


#基本用法
from multiprocessing import Process

import time,os

def task(x):
    print('%s is running'%x)
    print(os.getpid())
    time.sleep(5)

    print('%s is done'%x)


if __name__ == '__main__':
    p = Process(target=task,args=('任务1',))
    p.start()
    print(os.getpid())










