#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from threading import Thread,Lock
import time

mutex = Lock()

n = 100
def task():
    global n
    with mutex:
        temp = n
        time.sleep(0.1)
        n = temp -1


if __name__ == '__main__':
    t_l= []
    for i in range(100):
        t = Thread(target=task)
        t_l.append(t)
        t.start()

    for ti in t_l:
        ti.join()

    print(n)






