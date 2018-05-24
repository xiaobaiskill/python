#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


def student():
    from interface import student
    student_obj = student.student()
    student_view= {
        '1':student_obj.register
        ,'2':student_obj.pay_edu
        ,'3':student_obj.record
        ,'4':student_obj.cat_score
    }
    while True:
        print('''
-----欢迎进入学生视图-----
1.  注册
2.  交学费
3.  查看上课记录
4.  查看作业成绩
q.  返回
    ''')
        select = input('>>>').strip()
        if select == 'q':
            return None
        elif select in student_view:
            student_view[select]()


def teacher():
    from interface import teacher
    teacher_obj = teacher.teacher()
    teacher_view = {
        '1':teacher_obj.record_in_class
        ,'2':teacher_obj.make_score
        ,'3':teacher_obj.cat_record_in_class
        ,'4':teacher_obj.cat_score
    }
    while True:
        print('''
    -----欢迎进入讲师视图-----
    1.  创建上课记录
    2.  创建学员成绩
    3.  查看学员上课记录
    4.  查看学员成绩
    q.  返回''')
        select = input('>>>').strip()
        if select == 'q':
            return None
        elif select in teacher_view:
            teacher_view[select]()

def manager():
    from interface import school
    from interface import course
    from interface import teacher
    school_obj = school.school()
    course_obj = course.course()
    teacher_obj = teacher.teacher()

    manager_view = {
        '1': school_obj.index
        ,'2':teacher_obj.create_teacher
        ,'3':course_obj.create_course
    }
    while True:
        print('''
-----欢迎进入管理视图-----
1、校区管理
2、创建讲师
3、创建课程
q、返回
            ''')
        select = input('>>>').strip()
        if select == 'q':
            break
        elif select in manager_view:
            manager_view[select]()

