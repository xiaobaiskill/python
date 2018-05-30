#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from db import models

def create_course(course_name,school_name):
    school_obj =models.school.get_info_by_name(school_name)
    course_obj = models.course.get_info_by_name(course_name)

    if course_name: return False, '课程已存在'
    if not school_name:return False,'校区不存在'

    school_obj.add_course(course_name)
    models.course(course_name)
    return True,'课程创建成功'
