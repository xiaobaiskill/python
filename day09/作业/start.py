#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os,sys
from lib.common import echo
from core import src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


run_view={
    '1':src.user_run,
    '2':src.admin_run
}

def run():
    while True:
        print('''
----你的角色是----
      1、普通用户
      2、管理员
      q、退出
        ''')
        chooise = input('>>>').strip()
        if chooise =='q' : break
        if chooise in run_view:
            run_view[chooise]()
        else:
            echo('输入请重新选择')


if __name__ == '__main__':
    run()
