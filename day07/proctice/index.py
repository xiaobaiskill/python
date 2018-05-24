#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os,sys
from bin import main

sys.path.append(os.path.dirname(__file__))

view_obj = {
    '1': main.student
    ,'2': main.teacher
    ,'3': main.manager
}

while True:
    print('''
------欢迎进入选课系统------
1、学生视图
2、讲师视图
3、管理视图
q、退出
    ''')
    select = input('>>>').strip()
    if select == 'q':
        break
    if select in view_obj:
        view_obj[select]()
