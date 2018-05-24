#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from interface.school import school as school_obj
school_obj = school_obj()

class course:
    def __init__(self):
        pass
    def create_course(self,data):
        res =db_handle.add('course',data)
        if res:
            return True,'课程添加成功'
        else:
            return False,'课程添加失败'
    def cat_course(self):
        data = db_handle.select('course')
        if data:
            for k,info in enumerate(data):
                data[k].update(school_obj.cat_school_id(info['school_id']))
            return data
        pass
        

