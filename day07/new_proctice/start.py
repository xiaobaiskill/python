#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core import src

start_view = {
    '1':src.manager_run,
    '2':src.teacher_run,
    '3':src.student_run
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
        if chooise in start_view:
            start_view[chooise]()


if __name__ == '__main__':
    run()






