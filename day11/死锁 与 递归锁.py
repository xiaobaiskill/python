#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from threading import Thread,Lock,RLock
import time



# 死锁现象
mutexA = Lock()
mutexB = Lock()

class Mythread(Thread):
    def run(self):
        self.f1()
        self.f2()
    def f1(self):
        mutexA.acquire()
        print('%s 抢到了A锁'%(self.name))
        mutexB.acquire()
        print('%s 抢到了B锁' % (self.name))
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 抢到了A锁'%(self.name))
        time.sleep(1)
        mutexA.acquire()
        print('%s 抢到了B锁' % (self.name))
        mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = Mythread()
        t.start()
