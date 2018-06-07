#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib.common import echo
from interface import admin_interface
from interface import user_interface

admin_data = {}


def auth(func):
    '''
    我是装饰器
    :param func:
    :return:
    '''
    def wrapper(*args,**kwargs):
        if 'user' in admin_data:
            return func(*args,**kwargs)
        else:
            while True:
                admin = input('管理账号>>>').strip()
                pwd = input('管理密码>>>').strip()
                res, msg = admin_interface.login(admin, pwd)
                if res:
                    admin_data['user'] = msg['user']
                    echo('登陆成功')
                    return func(*args,**kwargs)
                else:
                    echo(msg)
                    continue
    return wrapper



def login():
    while True:
        admin = input('管理账号>>>').strip()
        pwd = input('管理密码>>>').strip()
        res,msg = admin_interface.login(admin,pwd)
        if not res:
            echo(msg)
            continue
        else:
            admin_data['user'] = msg['user']
            echo('登陆成功')
            break


@auth
def add_user():
    '''
    添加用户
    :return:
    '''
    while True:
        user = input('用户名>>>').strip()
        pwd = input('密码>>>').strip()
        pwd_again = input('再次确认密码>>>').strip()
        if user and pwd and pwd == pwd_again:
            data_size = input('用户空间大小（单位：bytes）>>>').strip()
            home_dir = input('家目录>>>').strip()
            if data_size and home_dir:
                res,msg = user_interface.add_user(user,pwd,data_size,home_dir)
                echo(msg)
                break
            else:
                echo('请输入完整信息')
                continue
        else:
            echo('两次密码不一致，请重新输入')
            continue



