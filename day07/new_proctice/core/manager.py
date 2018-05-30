#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib import common
from interface import manager_interface

manager_data = {}

def auth(func):
    '''
    我是装饰器
    :param func:
    :return:
    '''
    def wrapper(*args,**kwargs):
        if 'name' in manager_data:
            return func(*args,**kwargs)
        else:
            name = input('please input your name>').strip()
            pwd = input('please input your passwd>').strip()
            if name and pwd:
                status, msg = manager_interface.login(name,pwd)
                common.echo(msg)
                if status:
                    manager_data['name'] = name
                    return func(*args,**kwargs)
    return wrapper


def register():
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
            status,msg = manager_interface.register(name,pwd)
            manager_data = {'name':name}
            common.echo(msg)
        else:
            common.echo('两次密码输入不一致')
    else:
        common.echo('用户名密码不能为空')


def login():
    '''
    管理严登陆
    :return:
    '''
    name = input('please input your name>').strip()
    pwd = input('please input your passwd>').strip()
    if name and pwd:
        status,msg = manager_interface.login(name,pwd)
        if status:manager_data['name'] = name
        common.echo(msg)
    else:
        common.echo('请填写完整数据')
    pass

@auth
def create_school():
    school_name = input('please school name>').strip()
    school_addr = input('please school addr>').strip()
    if school_name and school_addr:
        status,msg = manager_interface.create_school(manager_data['name'],school_name,school_addr)

    else:
        common.echo('请输入完整的数据类型')
@auth
def create_teacher():
    pass

@auth
def create_course():
    pass



