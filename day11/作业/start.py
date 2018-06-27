#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from core import src

info = {
    '1':src.manger_run,
    '2':src.member_run
}
def run():
    while True:
        print('''
--------- 欢迎进入优酷 --------
    1、管理用户
    2、普通用户
    q、退出
        ''')
        chooise = input('>>>').strip()
        if chooise == q:break
        if chooise in info:
            info[chooise]()