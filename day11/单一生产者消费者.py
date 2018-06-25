#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from multiprocessing import Process,Queue
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
        if res is None:break
        time.sleep(random.randint(1,3))
        print('\033[09m消费者%s 吃了%s\033[14m'%(name,res))


if __name__ == '__main__':
    q = Queue()
    # 生成者们
    p1 = Process(target=producer,args=('jmz',q))

    # 消费者
    c1 = Process(target=concumer,args=('me',q))

    p1.start()
    c1.start()
    p1.join()
    q.put(None)

