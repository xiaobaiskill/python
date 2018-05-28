#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle

class scoreModel:
    def __init__(self):
        pass

    def add_student(self,data):
        '''
        添加学员的成绩
        :param data: {}
        :return:
        '''
        return db_handle.add('score',data)

    def cat_class_id(self,class_id):
        res = db_handle.select('score')
        data = []
        for info in res:
            if info['class_id'] == str(class_id):
                data.append(info)
        return data

    def cat_student(self,name):
        '''
        查看学员成绩
        :param name:
        :return:
        '''
        res = db_handle.select('score')
        data = []
        for info in res:
            if info['student_name'] == name:
                data.append(info)
        return data
