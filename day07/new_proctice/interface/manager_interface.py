#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib import common



def register(name,pwd):
    '''
    管理员注册
    :param name:
    :param pwd:
    :return:
    '''
    name =input('please input your name>').strip()
    pwd = input('please input your passwd>').strip()
    confirm_pwd = input('please input your confire passwd').strip()
    if name and pwd and confirm_pwd:
        if pwd == confirm_pwd:
            pass
        else:
            common.echo('两次密码输入不一致')
    else:
        common.echo('用户名密码不能为空')

    pass

def login(name,pwd):
    pass
