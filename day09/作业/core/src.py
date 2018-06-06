#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib.common import echo
from core import user

user_view = {
    '1':user.register,
    '2':user.login
}
def user_run():
    while True:
        print('''
    -----欢迎来到用户界面----
        1、注册
        2、登陆
        q、退出
        ''')
        chooise  = input('>>>').strip()
        if chooise == 'q':break
        if chooise in user_view:
            user_view[chooise]()
        else:
            echo('输入有误，请重新输入')

def admin_run():
    pass