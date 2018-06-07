#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib.common import echo
from core import user
from core import admin

user_view = {
    '1':user.login
}
def user_run():
    while True:
        print('''
-----欢迎来到用户界面----
    1、登陆
    q、退出
        ''')
        chooise  = input('>>>').strip()
        if chooise == 'q':break
        if chooise in user_view:
            user_view[chooise]()
        else:
            echo('输入有误，请重新输入')

admin_view ={
    '1':admin.login,
    '2':admin.add_user
}

def admin_run():
    while True:
        print('''
-----欢迎来到管理界面----
    1、登陆
    2、添加用户
    q、退出  
        ''')
        chooise = input('>>>').strip()
        if chooise == 'q':break
        if chooise in admin_view:
            admin_view[chooise]()
        else:
            echo('输入有误，请重新输入')