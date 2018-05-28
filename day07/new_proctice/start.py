#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from core import src

start_view = {
    '1':src.manager,
    '2':src.teacher,
    '3':src.student
}

def run():
    while True:
        print('''
------选课系统------
    1、管理视图
    2、老师视图
    3、学生视图        
    q、退出
        ''')
        chooise = input('>>>').strip()
        if chooise == 'q':break
        if chooise.isdigit() and int(chooise) <len(start_view):
            start_view[chooise]()


if __name__ == '__main__':
    run()






