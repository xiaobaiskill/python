#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import queue


# 先进先出
# q = queue.Queue()
# q.put('a')
# q.put('b')
# q.put('c')
# print(q.get())
# print(q.get())
# print(q.get())


# 先进后出
# q = queue.LifoQueue()
# q.put('1')
# q.put('2')
# q.put('3')
#
# print(q.get())
# print(q.get())
# print(q.get())

# 优先级, 等级越低越优先（级别,数据）
q = queue.PriorityQueue()
q.put((1,'a'))
q.put((11,'b'))
q.put((3,'c'))

print(q.get())
print(q.get())
print(q.get())
