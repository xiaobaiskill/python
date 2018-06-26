#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from  multiprocessing import Process,Lock
import json,os,time,random

# # 测试一，没有锁时
# # 排队 买票
# def buy_p():
#     with open('db.json','r',encoding='utf-8') as f:
#         data = json.load(f)
#     if int(data['count']) >0:
#         info = {}
#         info['count'] = int(data['count']) -1
#         time.sleep(random.randint(1,3))
#         with open('db.json','w',encoding='utf-8') as f:
#             json.dump(info,f)
#         print('%s 抢票成功'%os.getpid())
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=buy_p)
#         p.start()

'''
    没有锁的情况下，每一个都可以抢到票，数据不安全
'''

# 测试二，有锁时
# 排队 买票
mutex = Lock()
def buy_p(mutex):
    mutex.acquire()
    with open('db.json','r',encoding='utf-8') as f:
        data = json.load(f)
    if int(data['count']) >0:
        info = {}
        info['count'] = int(data['count']) -1
        time.sleep(random.randint(1,3))
        with open('db.json','w',encoding='utf-8') as f:
            json.dump(info,f)
        print('%s 抢票成功'%os.getpid())
    else:
        print('%s 抢票失败' % os.getpid())
    mutex.release()
if __name__ == '__main__':
    for i in range(10):
        p = Process(target=buy_p,args=(mutex,))
        p.start()


'''
测试二，在加锁的情况下可以保证数据的安全性，但失去了效率
'''



