#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import current_thread
import os,time,random

def get():
    time.sleep(random.randint(1,3))
    return os.getpid()

def echo(obj):
    res = obj.result()
    print('该进程的结果为%s'%res)

if __name__ == '__main__':

    # p = ProcessPoolExecutor()   # 默认是cpu 的核数
    # p_l = []
    # for i in range(10):
    #     obj = p.submit(get)    # 向操作系统发送信息的 是submit ,并生成对象
    #     p_l.append(obj)
    #
    # for obj in p_l:
    #     res = obj.result()     # result 等待对象的返回结果
    #     print('输入该进程的pid为：%s'%res)

    '''
        进程池中关于向操作系统发送信号的是submit与进程（start）不同
        进程池可返回结果，进程不能接受结果数据返回。
    '''



    # 回调函数

    p = ProcessPoolExecutor()

    for i in range(10):
        p.submit(get).add_done_callback(echo)  #回调函数会在任务运行完毕后自动触发，并且接收该任务对象
        # 分解：
        #     obj = p.submit()
        #     obj.add_done_callback(echo)
            # 讲解：
            #       p.submit 向操作系统发送创建进程信号。
            #       obj.add_done_callback(echo) 进程执行程序返回结果交于echo 执行

'''
    进程的返回结果是由主进程来执行程序的

'''



'''
    线程池关于 回调函数 与进程略微不同， 线程关于回调是 交给任意一个线程来执行的。而不是主线程（没有主子之分）

'''






