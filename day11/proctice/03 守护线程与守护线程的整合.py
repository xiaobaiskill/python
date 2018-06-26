#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from multiprocessing import Process
from threading import Thread
import os,time,random

def p_foo():
    print('守护进程 start')
    time.sleep(random.randint(1,3))
    print('守护进程 end')

def p_bar():
    print('子进程 start')
    time.sleep(random.randint(1,3))
    print('子进程 end')

def t_foo():
    print('守护线程 start')
    time.sleep(random.randint(1,3))
    print('守护线程 end')

def t_bar():
    print('非守护线程 start')
    time.sleep(random.randint(1, 3))
    print('非守护线程 end')

if __name__ == '__main__':
    p1 = Process(target=p_foo)
    p2 = Process(target=p_bar)
    p1.daemon =True

    t1 = Thread(target=t_foo)
    t2 = Thread(target=t_bar)
    t1.daemon = True

    p1.start()
    p2.start()
    t1.start()
    t2.start()
    print('主')

# 结果如下
    '''
守护线程 start
非守护线程 start
主
守护进程 start
子进程 start
非守护线程 end
子进程 end
    '''

    '''
守护线程 start
非守护线程 start
主
守护进程 start
子进程 start
守护线程 end
非守护线程 end
子进程 end
    '''

    '''
守护线程 start
非守护线程 start
主
守护进程 start
子进程 start
守护进程 end
守护线程 end
子进程 end
非守护线程 end
    '''


    '''
分析：
    在没有打印"主"之前线程快速起来并运行。其他线程遇到time.sleep,之后再执行该线程代码打印主
    在打印"主"之后并没结束，因为该进程的非守护线程的还没有结束（此时守护线程和进程还在进行中。。。因为"主"与"非守护线程"之间有其他线程进程打印）
    非守护线程结束后，后面还会在打印 子进程的数据但不会再打印守护线程或守护进程的数据了

总结：
    1、 守护线程会在 非守护线程运行结束时结束
    2、 守护进程会在主进程的所有非守护线程运行运行结束时结束
    
    '''