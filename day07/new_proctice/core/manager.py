#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib import common
from interface import manager_interface
from interface import school_interface
from interface import teacher_interface
from interface import course_interface


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
            while True:
                name = input('please input your name>').strip()
                pwd = input('please input your passwd>').strip()
                if name and pwd:
                    status, msg = manager_interface.login(name,pwd)
                    common.echo(msg)
                    if status:
                        manager_data['name'] = name
                        return func(*args,**kwargs)
                else:
                    common.echo('请输入完整的用户名密码')
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
            manager_data['name'] = name
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
    while True:
        name = input('please input your name>').strip()
        pwd = input('please input your passwd>').strip()
        if name and pwd:
            status,msg = manager_interface.login(name,pwd)
            common.echo(msg)
            if status:
                manager_data['name'] = name
                return None
        else:
            common.echo('请填写完整数据')

@auth
def create_school():
    '''
    创建校区
    :return:
    '''
    school_name = input('please school name>').strip()
    school_addr = input('please school addr>').strip()
    if school_name and school_addr:
        status,msg = school_interface.create_school(school_name,school_addr)
        common.echo(msg)
    else:
        common.echo('请输入完整的数据类型')

@auth
def create_teacher():
    '''
    创建讲师
    :return:
    '''
    school_data = school_interface.get_all_school()
    while True:
        for k,name in enumerate(school_data):
            print('%-30s%s'%(k,name))
        chooise_school = input('please input school number >').strip()
        if chooise_school.isdigit() and int(chooise_school) < len(school_data):
            school_name = school_data[chooise_school]
            while True:
                teacher_name = input('please input teacher name >').strip()
                if teacher_name:
                    status,msg = teacher_interface.create_teacher(school_name,teacher_name)
                    common.echo(msg)
                    return None
                else:
                    common.echo('请正确填写老师姓名')
        else:
            common.echo('选择信息有误,重新选择')

@auth
def create_course():
    '''
    创建课程
    :return:
    '''
    school_list = school_interface.get_all_school()
    while True:
        print('%-20s%s' % ('id','school_name'))
        for k,name in enumerate(school_list):
            print('%-20s%s'%(k,name))
        chooise_teacher = input('please input school id>>>').strip()
        if chooise_teacher.isdigit() and int(chooise_teacher) <len(school_list):
            school_name = school_list[chooise_teacher]
            while True:
                course_name = input('please course name >').strip()
                if course_name:
                    status,msg=course_interface.create_course(course_name,school_name)
                    common.echo(msg)
                    return None
                else:
                    common.echo('请正确输入课程名')
        else:
            common.echo('请输入正确的讲师id')



