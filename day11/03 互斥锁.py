#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from multiprocessing import Process,Lock
import json,time,random,os

def check():
    with open('db.json','rt',encoding='utf-8') as f:
        dic = json.load(f)
    print('%s 当前剩余票数 %s'%(os.getpid(),dic['count']))

def get():
    with open('db.json','rt',encoding='utf-8') as f:
        dic = json.load(f)
        time.sleep(1)
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(random.randint(1,3))
        with open('db.json','w',encoding='utf-8') as f:
            json.dump(dic,f)

        print('%s 抢票成功'%os.getpid())

def task(metex):
    # 查票
    check()
    # 抢票
    metex.acquire()
    get()
    metex.release()



if __name__ == '__main__':
    metex = Lock()
    for k in range(10):
        p = Process(target=task,args=(metex,))
        p.start()



