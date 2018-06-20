#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib.common import echo
from core import shell
from core import hosts


func_view = {
    '1':hosts.run,
    '2':shell.run
}

def run():
    while True:
        print('''
--------主机批量管理----
    1、主机管理
    2、进入命令窗口
    q、退出
        ''')
        chooise = input('>>>').strip()
        if chooise == 'q': break
        if chooise in func_view:
            func_view[chooise]()
            continue
        echo('内容有误')
