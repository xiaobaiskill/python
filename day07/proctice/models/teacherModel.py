#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from models.schoolModel import schoolModel
schoolModel_obj = schoolModel()


class teacherModel:
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
                data[k].update(schoolModel_obj.cat_school_id(info['school_id']))
            return data
    def cat_teacher_id(self,id):
        res = db_handle.select('teacher')
        data = res[int(id)]
        data.update(schoolModel_obj.cat_school_id(data['school_id']))
        return data

if __name__ == '__main__':
    teacher_obj = teacherModel()
    print(teacher_obj.cat_teacher())