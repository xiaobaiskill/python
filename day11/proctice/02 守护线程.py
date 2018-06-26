#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from threading import Thread
import os, time, random

def foo():
    print('foo start')
    time.sleep(random.randint(1, 3))
    print('foo end')

def bar():
    print('bar start')
    time.sleep(random.randint(1, 3))
    print('bar end')

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.daemon =True    # 表示P1 是守护进程
    t2.start()
    t1.start()
    print('主')

    # 有可能会遇到下面两种情况
    '''
    bar start
    foo start
    主
    foo end
    bar end
    '''

    '''
    bar start
    foo start
    主
    bar end
    '''

'''
一个进程内可以有多个线程，线程即执行程序，只有执行程序都执行完了，那这个进程才没有存在的意思。
一个进程的一诞生就存在一个线程，这个线程伴随着这个进程的始终。
这个线程的生命周期，代表着整个进程的生命周期。由它衍生出的其他非守护线程都有它管理。只有其他非守护线程死掉，它才可以死掉
它的死亡以为着守护线程的命运结束

上面的结果也证明了这一点，在运行完这个线程的代码时，它会等待其他的飞守护线程（t2）运行完毕，非守护线程结束，该线程也就
结束了，接着守护线程的命运也结束了。
'''

