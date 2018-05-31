#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import models

def register(name,pwd):
    '''
    学生注册接口
    :param name:
    :param pwd:
    :return:
    '''
    if models.student.get_info_by_name(name):
        return False,'学员已存在'
    else:
        models.student(name,pwd)
        return True,'学员注册成功'

def login(name,pwd):
    '''
    学生登录
    :param name:
    :param pwd:
    :return:
    '''
    student_data = models.student.get_info_by_name(name)
    if student_data.pwd == pwd:
        return True,'登录成功'
    else:
        return False,'用户名或密码不一致'

def school_chooise(name,school_name):
    '''
    校区选择 接口
    :param name:
    :param school_name:
    :return:
    '''
    student_info = models.student.get_info_by_name()
    if student_info:
        if student_info.add_school(school_name):
            return True,'校区选择成功'
        else:
            return False,'校区选择失败，请确认是否已选择过校区'
    else:
        return False,'学生不存在'
    pass

def get_info(name):
    '''
    获取学生信息
    :param name:
    :return:
    '''
    return models.student.get_info_by_name(name)

def chooise_course(name,course_name):
    course_info = models.course.get_info_by_name(course_name)
    student_info = models.student.get_info_by_name(name)
    if not course_info: return False,'课程不存在'
    status = student_info.add_course(course_name)
    course_info.add_student(name)
    if status:
        return True,'课程添加成功'
    else:
        return False,'课程已存在'


def save_score(name,course_name,score):
    student_info = models.student.get_info_by_name(name)
    return student_info.add_score(course_name,score)