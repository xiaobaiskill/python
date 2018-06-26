#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


from multiprocessing import Process
import os,time,random


def foo():
    print('foo start')
    time.sleep(random.randint(1,3))
    print('foo end')

def bar():
    print('bar start')
    time.sleep(random.randint(1, 3))
    print('bar end')

if __name__ == '__main__':

    # 测试一
    # p1 = Process(target=foo)
    # p2 = Process(target=bar)
    #
    # p1.daemon =True    # 表示P1 是守护进程
    # p1.start()
    # p2.start()
    # print('主')

    '''
    主
    bar start
    bar end
    '''

    # 测试二
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.daemon =True    # 表示P1 是守护进程
    p1.start()
    p2.start()
    time.sleep(1)
    print('主')
    '''
    foo start
    bar start
    主
    bar end
    '''



'''

分析：
    第一次的测试并没有打印守护进程(p1)的 数据，子进程p2的数据都打印了
    第二次测试 在主进程打印"主"之前停了1秒 守护进程打印出来了"foo start",后面"foo end"没有打印，子进程p2的数据都打印了
结论：
    1、守护进程与子进程无关，只与主进程有关（无论守护进程怎样，子进程都没有变化）
    2、守护进程与主进程的执行时间有关。
    
总结：
    该进程的所有非守护线程运行结束，守护进程就会结束（主进程代码，不包含非守护进程代码）
    
    
'''




