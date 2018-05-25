#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle

class schoolModel:
    def __init__(self):
        pass
    def create_school(self,name,addr):
        data = {'school_name':name,'addr':addr,'action':1}
        res = db_handle.add('school',data)
        if res:
            return True,'添加成功'
        else:
            return False,'添加失败'

    def cat_school(self):
        '''
        查找全部的学校信息
        :return:
        '''
        return db_handle.select('school')

    def cat_school_id(self,id):
        '''
        查询下标ID的school 信息
        :param id:
        :return:
        '''
        data = db_handle.select('school')
        if data:
            return data[int(id)]

    def create_class(self,class_name,course_id,teacher_id):
        data = {'class_name':class_name,'course_id':course_id,'teacher_id':teacher_id}
        res = db_handle.add('class',data)
        if res:
            return True,'班级添加成功'
        else:
            return False,'班级添加失败'

