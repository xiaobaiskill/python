#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from multiprocessing import Process,JoinableQueue
import time,random


def producer(name,q):
    for i in range(5):
        res = '包子%s'%i
        print('\033[33m厨师%s 生成了一个%s\033[03m'%(name,res))
        time.sleep(random.randint(1,3))
        q.put(res)

def concumer(name,q):
    while True:
        res = q.get()
        time.sleep(random.randint(1,3))
        print('\033[09m消费者%s 吃了%s\033[14m'%(name,res))
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()

    # 生成者们
    p1 = Process(target=producer,args=('jmz',q))
    p2 = Process(target=producer,args=('aaa',q))
    p3 = Process(target=producer,args=('bbb',q))

    # 消费者
    c1 = Process(target=concumer,args=('xxx',q))
    c2 = Process(target=concumer,args=('yyy',q))
    c1.daemon =True
    c2.daemon =True

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    p1.join()
    q.join()
    print('主')

