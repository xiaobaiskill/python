#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 守护进程 是在主进程代码结束后 ，即立即死掉


from multiprocessing import Process
import os,time,random

def task():
    print('%s s runnig'%os.getpid())
    time.sleep(random.randint(1,3))
    print('%s is stop'%os.getpid())



if __name__ == '__main__':
    p1 =Process(target=task)
    p2 = Process(target=task)
    p1.daemon =True
    p1.start()
    p2.start()
    time.sleep(0.1)
    print('主')
'''
99320 s runnig
99321 s runnig
主
99321 is stop
'''

