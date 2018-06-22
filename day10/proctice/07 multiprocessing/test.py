
#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import time,os
from multiprocessing import Process

def test(count):
    time.sleep(10)
    print(os.getpid())



if __name__ == '__main__':
    p_l = []
    for k in range(3):
        p = Process(target=test,args=('1',))
        p_l.append(p)

    for m in p_l:
        m.start()