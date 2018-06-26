#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from threading import Thread
from multiprocessing import Process


print('我执行了一次')

def task_process():
    '''
    子进程需要复制一份主进程代码，同时执行自己的任务
    :return:
    '''
    print('进程会再执行文件代码')

def task_thread():
    '''
    多的线程公用同一份资源，无需在复制资源，只执行自己的代码
    :return:
    '''
    print('线程不会再执行此文件代码?')


if __name__ == '__main__':
    # t = Thread(target=task_thread)
    # t.start()
    # print('主')

    p= Process(target=task_process)
    p.start()


