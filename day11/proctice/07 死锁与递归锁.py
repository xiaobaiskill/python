#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from threading import Thread,Lock,RLock
import json,os,time,random

# Lock 用法，  每实力化一次就产生一把新的锁，锁直接没有关联。
# mutexA = Lock()
# mutexB = Lock()

# 递归锁使用类， 层层递归，每加一次锁就计数+1
mutexA = mutexB = RLock()



class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()
    def f1(self):
        mutexA.acquire()
        print('%s A锁占用中'%self.name)
        mutexB.acquire()
        print('%s B锁占用中'%self.name)
        time.sleep(1)
        print('%s B锁释放'%self.name)
        mutexB.release()
        print('%s A锁释放'%self.name)
        mutexA.release()
    def f2(self):
        mutexB.acquire()
        print('%s B锁占用中'%self.name)
        mutexA.acquire()
        print('%s A锁占用中'%self.name)
        time.sleep(1)
        print('%s A锁释放'%self.name)
        mutexA.release()
        print('%s B锁释放'%self.name)
        mutexB.release()

if __name__ == '__main__':
    for i in range(3):
        p = MyThread()
        p.start()

'''
Thread-1 A锁占用中
Thread-1 B锁占用中
Thread-1 B锁释放
Thread-1 A锁释放
Thread-2 A锁占用中
Thread-1 B锁占用中
'''
'''
Thread-1 A锁占用中
Thread-1 B锁占用中
Thread-1 B锁释放
Thread-1 A锁释放
Thread-1 B锁占用中
Thread-2 A锁占用中
'''
# 下面还有其他情况


'''
产生原因：
        Thread-2 A锁占用中
        Thread-1 B锁占用中
        
        锁时需要不同的进程之间抢的，
            Thread-1 A锁占用中
            Thread-1 B锁占用中
            Thread-1 B锁释放
            Thread-1 A锁释放
        线程1 在执行self.f1()时速度快，一下抢到了A锁B锁，但self.f2时抢到了B锁，但在抢A的过程中，被线程2抢到了。
        
        内部抢锁的过程，可能涉及到 先抢先得 的算法在里面。
'''


'''
    Lock  会产生 死锁现象，
    RLock 递归锁，计数加锁

'''


