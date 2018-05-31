#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib import common
from interface import teacher_interface
from interface import course_interface
from interface import student_interface

teacher_data = {}

def auth(func):
    def wrapper(*args,**kwargs):
        if teacher_data['name']:
            return func(*args,**kwargs)
        else:
            name = input('please input your name >').strip()
            pwd = input('please input your passwd >').strip()
            if name and pwd:
                status, msg = teacher_interface.login(name, pwd)
                common.echo(msg)
                if status:
                    teacher_data['name'] = name
                    common.echo('请填写完整信息')
            else:
                common.echo('请填写完整信息')



def login():
    while True:
        name = input('please input your name >').strip()
        pwd = input('please input your passwd >').strip()
        if name and pwd:
            status,msg = teacher_interface.login(name,pwd)
            common.echo(msg)
            if status:
                teacher_data['name'] = name
                return None
        else:
            common.echo('请填写完整信息')


@auth
def cat_course():
    '''
    查看课程
    :return:
    '''
    status,course_list = teacher_interface.cat_course(teacher_data['name'])
    common.echo(course_list)

@auth
def chooise_course():
    '''
    选择课程
    :return:
    '''
    course_list = course_interface.cat_course()
    if course_list:
        print('%-20s%s'%('id','课程名'))
        for k,name in enumerate(course_list):
            print('%-20s%s'%(k,name))
        chooise_course = input('please chooise your course >').strip()
        if chooise_course and chooise_course.isdigit() and int(chooise_course)<len(course_list):
            status,msg = teacher_interface.add_course(teacher_data['name'],course_list[int(chooise_course)])
            common.echo(msg)
        else:
            common.echo('请输入正确的指令')
    else:
        common.echo('请先创建课程')

@auth
def cat_course_student():
    '''
    查看课程学生
    :return:
    '''
    status, course_list = teacher_interface.cat_course(teacher_data['name'])
    if status:
        print('%-20s%s'%('id','课程名'))
        for k,name in enumerate(course_list):
            print('%-20s%s'%(k,name))
        chooise_course = input('please your course name >').strip()
        if chooise_course == 'q':return None
        if chooise_course and chooise_course.isdigit() and int(chooise_course)<len(course_list):
            status,msg = course_interface.cat_course_student(course_list[int(chooise_course)])
            common.echo(msg)
        else:
            common.echo('请输入正确的课程id')
    else:
        common.echo(course_list)


@auth
def save_student_score():
    '''
    修改学生的成绩
    :return:
    '''
    status, course_list = teacher_interface.cat_course(teacher_data['name'])
    if status:
        while True:
            print('%-20s%s' % ('id', '课程名'))
            for k, name in enumerate(course_list):
                print('%-20s%s' % (k, name))
            chooise_course = input('please your course name >').strip()
            if chooise_course =='q' :break
            if chooise_course and chooise_course.isdigit() and int(chooise_course) <len(course_list):
                course_name = course_list[int(chooise_course)]
                status,msg = course_interface.cat_course_student(course_name)
                if status:
                    while True:
                        print('%-20s%s'%('id','学生名'))
                        for k,name in  enumerate(msg):
                            print('%-20s%s'%(k,name))
                        chooise_student = input('please your student name >').strip()
                        if chooise_student == 'q':break
                        if chooise_student and chooise_student.isdigit() and int(chooise_student) <len(msg):
                            student_name = msg[int(chooise_student)]
                            score = input('please inpur student score >').strip()
                            if student_interface.save_score(student_name,course_name,score):
                                common.echo('成绩修改成功')
                            else:
                                common.echo('成绩修改失败')
                        else:
                            common.echo('请输入正确的学生id')
                else:
                    common.echo(msg)
            else:
                common.echo('请输入正确的指令')
    else:
        common.echo('请先选择课程')

    pass
