#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from interface import user_interface
from lib.common import echo
from ftp import client

user_data = {}
def login():
    while True:
        user = input('登陆名>>>').strip()
        pwd = input('密码>>>').strip()
        res,msg = user_interface.login(user,pwd)
        if res:
            user_data['user'] = msg['user']
            from ftp import client
            echo('登陆成功')
            echo('''-----欢迎进入ftp管理页面-----''')
            client = client.client_ftp(msg)
            client.run()

            return True
        else:
            echo(msg)
            continue




