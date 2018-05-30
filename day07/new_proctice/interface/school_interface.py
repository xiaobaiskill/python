#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import os
from config import setting
from db import models

def get_all_school():
    school_list = os.listdir('%s/school'%(setting.DB_DIR))
    return school_list


def create_school(school_name,school_addr):
    if not models.school.get_info_by_name(school_name):
        models.school(school_name,school_addr)
        return True,'校区创建成功'
    else:
        return False,'学校以存在'
