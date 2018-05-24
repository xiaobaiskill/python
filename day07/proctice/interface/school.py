#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


class school:
    def __init__(self):
        pass
    def index(self):
        '''
        教室管理页面
        :return:
        '''
        school_view = {
            '1':self.create_school
            ,'2':self.create_class
        }
        while True:
            print('''
-----欢迎进入学校管理页面            
1、创建校区
2、创建班级            
q、返回
            ''')
            select = input('>>>').strip()
            if select =='q':
                return None
            elif select in school_view:
                school_view[select]()

    def create_school(self):

        pass
    def create_class(self):
        '''
        创建班级
        :return:
        '''
        pass