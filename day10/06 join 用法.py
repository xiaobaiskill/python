#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 基础用法1
# from multiprocessing import Process
#
# import time,os
#
# def task(x):
#     print('%s is running'%x)
#     print(os.getpid())
#     time.sleep(5)
#     print('%s is done'%x)
#
#
# if __name__ == '__main__':
#     p = Process(target=task,args=('任务1',))
#     p.start()
#     p.join()    # 等待进程完成后再执行下面的程序
#
#     print('主',os.getpid())







# 基础用法二
# 多子进程 等待 时间。
# from multiprocessing import Process
#
# import time,os
#
# def task(x):
#     print('%s is running'%x)
#     print(os.getpid())
#     time.sleep(5)
#     print('%s is done'%x)
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     p1 = Process(target=task,args=('任务1',))
#     p1.start()
#
#     p2 = Process(target=task, args=('任务1',))
#     p2.start()
#
#     p3 = Process(target=task, args=('任务1',))
#     p3.start()
#
#     p1.join()    # 等待进程完成后再执行下面的程序
#     p2.join()
#     p3.join()
#
#     stop_time=time.time()
#     print(stop_time-start_time)
#     print('主',os.getpid())



# 简单用法三
from multiprocessing import Process

import time,os

def task(x):
    print('%s is running'%os.getpid())
    time.sleep(x)


if __name__ == '__main__':
    start_time = time.time()
    p_l=[]
    for k in range(1,3):
        p = Process(target=task,args=(k,))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()
    stop_time=time.time()
    print(stop_time-start_time)
    print('主',os.getpid())

