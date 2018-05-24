#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from interface.school import school as school_obj
school_obj = school_obj()


class teacher:
    def __init__(self):
        pass
    def create_teacher(self,data):
        res = db_handle.add('teacher',data)
        if res:
            return True,'讲师添加成功'
        else:
            return False,'讲师添加失败'

    def cat_teacher(self):
        data = db_handle.select('teacher')
        if data:
            for k,info in enumerate(data):
                data[k].update(school_obj.cat_school_id(info['school_id']))
            return data


if __name__ == '__main__':
    teacher_obj = teacher()
    print(teacher_obj.cat_teacher())