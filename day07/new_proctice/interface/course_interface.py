#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import os
from db import models
from config import setting

def create_course(course_name,school_name):
    '''
    创建课程
    :param course_name:
    :param school_name:
    :return:
    '''
    school_obj =models.school.get_info_by_name(school_name)
    course_obj = models.course.get_info_by_name(course_name)

    if course_obj: return False, '课程已存在'
    if not school_name:return False,'校区不存在'

    school_obj.add_course(course_name)
    models.course(course_name)
    return True,'课程创建成功'

def cat_course():
    '''
    查看所有的课程
    :return:
    '''
    course_list = os.listdir('%s/course' % (setting.DB_DIR))
    return course_list

def cat_course_student(course_name):
    course_info = models.course.get_info_by_name(course_name)
    if course_info:
        if course_info.student_list:
            return True,course_info.student_list
        else:
            return False,'该课程还没有学生'
    else:
        return True,'课程不存在'
