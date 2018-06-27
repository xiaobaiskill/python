#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from multiprocessing import Process,JoinableQueue
import os,random,time

def producer(q):
    for i in range(random.randint(3,6)):
        res = '包子%s'%i
        time.sleep(random.randint(1, 3))
        q.put(res)
        print('\033[24m%s厨师生产了%s\033[35m'%(os.getpid(),res))



def consumer(q):
    while True:
        res = q.get()
        print('%s老板吃了%s'%(os.getpid(),res))
        q.task_done()
        time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    q = JoinableQueue()
    producer_l = []
    for i in range(3):
        p = Process(target=producer,args=(q,))
        p.start()
        producer_l.append(p)

    consumer_l = []
    for i in range(2):
        p = Process(target=consumer,args=(q,))
        p.daemon = True
        p.start()
        consumer_l.append(p)

    for p in producer_l:
        p.join()      # 首先保证所有的生产者都生产完包子
    q.join()  # 1、证明生产者都已经完全生产完毕 2、队列为空，也就是消费者也消费完毕
    print('zhu')


'''
多个生成者和消费者的解决方案。

多个生产者生产数据，并保证数据都生产完毕（p.join）

多个消费者消费数据，并保证队列中的数据都消费完毕（q.join == JoinableQueue().join）

'''



