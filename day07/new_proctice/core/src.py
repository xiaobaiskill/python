#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

def manager():
    from core import manager
    manager_view = {
        '1':manager.register,
        '2':manager.login,
        '3':manager.create_school,
        '4':manager.create_teacher,
        '5':manager.create_course
    }

    while True:
        print('''
-------管理视图-----
    1、注册
    2、登录
    3、创建校区
    4、创建讲师
    5、创建课程
        ''')
        chooise = input('>>>').strip()
        if chooise.isdigit() and int(chooise) < len(manager_view):
            manager_view[chooise]()




def teacher():
    from core import teacher
    teacher_view = {
        '1':teacher.login,
        '2':teacher.cat_course,
        '3':teacher.chooise_course,
        '4':teacher.cat_course,
        '5':teacher.save_student_score
    }

    while True:
        print('''
------教师视图-----
    1、登录
    2、查看授课教程
    3、选择授课教程
    4、查看课程下学生
    5、修改学生成绩
    q、返回 
        ''')
        chooise = input('>>>').strip()
        if chooise =='q':break
        if chooise.isdigit() and int(chooise) < len(teacher_view):
            teacher_view[chooise]()





def student_run():
    from core import student
    student_view = {
        '1':student.register,
        '2':student.login,
        '3':student.school_chooise,
        '4':student.course_chooise,
        '5':student.cat_score
    }
    while True:
        print('''
------学生视图-----
    1、注册
    2、登录
    3、选择校区
    4、选择课程
    5、查看成绩
    q、返回
''')
        chooise= input('>>>').strip()
        if chooise =='q':break
        if chooise.isdigit() and int(chooise) < len(student_view):
            student_view[chooise]()

