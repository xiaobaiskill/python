#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from threading import Thread,Lock
import json,os,time,random

mutex = Lock()
def buy_p():
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
        p = Thread(target=buy_p)
        p.start()


'''
    线程与进程都一样，使用方式也一样
'''
