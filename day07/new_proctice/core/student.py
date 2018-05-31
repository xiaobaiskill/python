#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib import common
from interface import student_interface
from interface import school_interface


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

@auth
def school_chooise():
    '''
    选择学校
    :return:
    '''
    school_list = school_interface.get_all_school()
    while True:
        print('%-20s%s'%('id','校区名'))
        for k,name in enumerate(school_list):
            print('%-20s%s'%(k,name))
        chooise_school = input('please your chooise school_id >').strip()
        if chooise_school:
            if chooise_school.isdigit() and int(chooise_school) <len(school_list):
                school_name = school_list[int(chooise_school)]
                status,msg = student_interface.school_chooise(student_data['name'],school_name)
                common.echo(msg)
        common.echo('请输入正确的校区id')

@auth
def course_chooise():
    '''
    选择课程
    :return:
    '''
    student_info = student_interface.get_info(student_data['name'])
    if student_info.school_name:
        course_list = school_interface.get_school_course(student_info.school_name)
        if course_list:
            while True:
                print('%-20s%s'%('id','课程名称'))
                for k,name in enumerate(course_list):
                    print('%-20s%s'%(k,name))
                chooise_course = input('please chooise your course id >').strip()
                if chooise_course and chooise_course.isdigit() and int(chooise_course) <len(course_list):
                    course_name = course_list[int(chooise_course)]
                    status,msg = student_interface.chooise_course(student_data['name'],course_name)
                    common.echo(msg)
                    if status:
                        return None
            else:
                common.echo('请输入正确的指令')
        else:
            common.echo('暂无课程可选')
    else:
        common.echo('请先选择校区')
    pass

@auth
def cat_score():
    '''
    查看成绩
    :return:
    '''
    student_info =student_interface.get_info(student_data['name'])
    if student_info:
        if student_info.score:
            common.echo(student_info.score)
        else:
            common.echo('暂无成绩')
    else:
        common.echo('学生不存在')