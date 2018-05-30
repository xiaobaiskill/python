#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os
from config import setting
from db import models

def get_all_teacher():
    teacher_list = os.listdir('%s/teacher' % (setting.DB_DIR))
    if teacher_list:
        teacher_data =[]
        for teacher in teacher_list:
            teacher_info = models.teacher.get_info_by_name(teacher)
            teacher_data.append({'name':teacher_info.name,'school_name':teacher_info.school_name})
        return teacher_data
    else:
        return None


def create_teacher(school_name,teacher_name):
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
            models.teacher(teacher_name, school_name)
            return True,'讲师创建成功'
        else:
            return False,'校区不存在'




