#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os
from config import setting
from db import models

def get_all_teacher():
    '''
    获取所有老师的数据
    :return:
    '''
    teacher_list = os.listdir('%s/teacher' % (setting.DB_DIR))
    if teacher_list:
        teacher_data =[]
        for teacher in teacher_list:
            teacher_info = models.teacher.get_info_by_name(teacher)
            teacher_data.append({'name':teacher_info.name,'school_name':teacher_info.school_name})
        return teacher_data
    else:
        return None


def create_teacher(school_name,teacher_pwd,teacher_name):
    '''
    创建讲师
    :param school_name:
    :param teacher_name:
    :return:
    '''
    if models.teacher.get_info_by_name(teacher_name):
        return False,'讲师已存在'
    else:
        school_data = models.school.get_info_by_name(school_name)
        if school_data:
            school_data.add_teacher(teacher_name)
            models.teacher(teacher_name, teacher_pwd,school_name)
            return True,'讲师创建成功'
        else:
            return False,'校区不存在'

def login(name,pwd):
    '''
    登陆
    :param name:
    :param pwd:
    :return:
    '''
    teacher_info = models.teacher.get_info_by_name(name)
    if teacher_info:
        if teacher_info.pwd == pwd:
            return True,'登陆成功'
    return False,'用户名和密码错误'


def cat_course(name):
    '''
    查看老师课程
    :param name:
    :return:
    '''
    teacher_info = models.teacher.get_info_by_name(name)
    if teacher_info:
        if teacher_info.course_list:
            return True,teacher_info.course_list
        else:
            return False,'请先选择课程'
    else:
        return False,'讲师不存在'
    pass

def add_course(name,course_name):
    '''
    添加课程
    :param name:
    :param course_name:
    :return:
    '''
    course_info = models.course.get_info_by_name(course_name)
    teacher_info = models.teacher.get_info_by_name(name)
    if not course_name:return False,'课程不存在'
    if not teacher_info:return False,'讲师不存在'
    if course_info.teacher_name:return False,'课程已存在讲师'
    status,msg = teacher_info.add_course(course_name)
    if status:
        course_name.add_teacher(name)
    return status,msg


