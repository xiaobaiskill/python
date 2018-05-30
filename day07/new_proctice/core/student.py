#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib import common
from interface import student_interface


student_data = {}
def auth(func):
    def wrapper(*args,**kwargs):
        if 'name' in student_data:
            return func(*args,**kwargs)
        else:
            while True:
                name = input('please input your name>').strip()
                pwd = input('please input your passwd>').strip()
                if name and pwd:
                    status, msg = student_interface.login(name, pwd)
                    common.echo(msg)
                    if status:
                        student_data['name'] = name
                        return func(*args, **kwargs)
                else:
                    common.echo('请输入完整的用户名密码')
    return wrapper


def register():
    '''
    学员注册
    :return:
    '''
    name =input('please input your name>').strip()
    pwd = input('please input your passwd>').strip()
    confirm_pwd = input('please input your confire passwd').strip()
    if name and pwd and confirm_pwd:
        if pwd == confirm_pwd:
            status,msg = student_interface.register(name,pwd)
            student_data['name'] = name
            common.echo(msg)
        else:
            common.echo('两次密码输入不一致')
    else:
        common.echo('用户名密码不能为空')


def login():
    '''
    学员登录
    :return:
    '''
    while True:
        name = input('please input your name>').strip()
        pwd = input('please input your passwd>').strip()
        if name and pwd:
            status,msg = student_interface.login(name,pwd)
            common.echo(msg)
            if status:
                student_data['name'] = name
                return None

        else:
            common.echo('请填写完整数据')


def school_chooise():
    pass

def course_chooise():
    pass

def cat_score():
    pass