#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 1、守护线程 是 等待所有的非守护线程 运行结束后，死掉
# 2、主线程的声明周期代表者进程的生命周期

from threading import Thread
import os,time,random

def task():
    print('%s s runnig'%os.getpid())
    time.sleep(random.randint(1,3))
    print('%s is stop'%os.getpid())



if __name__ == '__main__':
    t1 =Thread(target=task)
    t2 = Thread(target=task)
    t1.daemon =True
    t1.start()
    t2.start()
    print('主')

'''
等待 t2 非守护线程完成后，此时整个线程才算结束。
'''


'''
结构可能有两种
99373 s runnig
99373 s runnig
主
99373 is stop


或

99418 s runnig
99418 s runnig
主
99418 is stop
99418 is stop
'''

