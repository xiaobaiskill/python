#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


def student():
    from core import student
    student_obj = student.student()
    student_view= {
        '1':student_obj.register
        ,'2':student_obj.login
    }
    while True:
        print('''
-----欢迎进入学生视图-----
1.  注册
2.  登陆
q.  返回
    ''')
        select = input('>>>').strip()
        if select == 'q':
            return None
        elif select in student_view:
            student_view[select]()


def teacher():
    from core import teacher
    teacher_obj = teacher.teacher()
    teacher_view = {
        '1': teacher_obj.class_management
    }
    while True:
        print('''
    -----欢迎进入讲师视图-----
    1.  班级管理
    q.  返回''')
        select = input('>>>').strip()
        if select == 'q':
            return None
        elif select in teacher_view:
            teacher_view[select]()

def manager():
    from core import school
    from core import teacher
    from core import student
    school_obj = school.school()
    teacher_obj = teacher.teacher()
    student_obj = student.student()
    manager_view = {
        '1': school_obj.index
        ,'2':teacher_obj.create_teacher
        ,'3':school_obj.create_course
        ,'4':student_obj.register
    }
    while True:
        print('''
-----欢迎进入管理视图-----
1、校区管理
2、创建讲师
3、创建课程
4、创建学员
q、返回
            ''')
        select = input('>>>').strip()
        if select == 'q':
            break
        elif select in manager_view:
            manager_view[select]()

