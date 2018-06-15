#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os,time
from multiprocessing import Process,Lock

def work(lock):
    lock.acquire()
    print('%s is running'%os.getpid())
    time.sleep(1)
    print('%s is stop'%os.getpid())
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work,args=(lock,))
        p.start()


'''
进程加锁 lock
好处：
    1、后期信息处理不会出现信息错乱的情况，因为每次只会有一个进程在执行work，
    例如：比如web开发人员写一个进程代码，读取mysql中的
    
坏处：
    1、同一件事只能一个进程做，多进来一个进程就会处理等待状态，牺牲了效率。

'''




