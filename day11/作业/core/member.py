#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib.common import echo
from interface import member_interface

# 装饰器
def auth(func):
    pass


def register():
    while True:
        user = input('输入姓名：').strip()
        passwd = input('输入密码').strip()
        confirm_passd = input('再次确认密码').strip()
        if passwd == confirm_passd:
            if not passwd:
                echo('密码不能为空')
                continue
            member_interface.register(user,passwd)


        else:
            echo('两次密码不一致')


def login():
    pass

@auth
def buy_vip():
    pass

@auth
def cat_video():
    pass

@auth
def download_video():
    pass

@auth
def cat_video_log():
    pass

@auth
def cat_notice():
    pass
