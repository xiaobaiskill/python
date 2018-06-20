#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from core import shell
from interface import hosts_interface

def add_host():
    pass

def cat_host():
    pass


func_view = {
    '1':add_host,
    '2':cat_host,
    '3':shell.run
}

def run():
    while True:
        print('''
--------主机批量管理----
    1、添加主机
    2、查看主机
    3、进入命令窗口
    q、退出
        ''')
        chooise = input('>>>').strip()
        if chooise == 'q': break
        if chooise in func_view:
            func_view[chooise]()
