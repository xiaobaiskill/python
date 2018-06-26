#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from multiprocessing import Process,Semaphore
# from  threading import  Thread,Semaphore
import os,time,random

'''
主要做了解
信号量 每次最多可以使用进程的个数， 后期会使用进程池，只做了解

进程与线程用法一致

进程中的用法与线程一致
'''
sm = Semaphore(4)   # 一次只开启四个进程数

def go_wc(sm):
    sm.acquire()
    print('%s 正在启动中'%os.getpid())
    time.sleep(random.randint(1,3))
    sm.release()

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=go_wc,args=(sm,))
        p.start()

        # t = Thread(target=go_wc, args=(sm,))
        # t.start()



