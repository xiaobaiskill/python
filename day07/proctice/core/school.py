#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from common import func
from interface.school import school as school_obj
from interface.course import course as course_obj
from interface.teacher import  teacher as teacher_obj

course_obj = course_obj()
school_obj = school_obj()
teacher_obj = teacher_obj()

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
        '''
        创建校区
        :return:
        '''
        name = input('校名：').strip()
        addr = input('地址：').strip()
        if name != '' and addr != '':
            res,msg = school_obj.create_school(name,addr)
            func.echo(msg)
        else:
            func.echo('校名或地址不能为空')

    def create_class(self):
        '''
        创建班级
        :return:
        '''
        course_data = course_obj.cat_course()
        if course_data:
            for i,course_info in enumerate(course_data):
                print(i,course_info['course_name'],course_info['addr'])
        else:
            func.echo('课程不存在，请先创建课程')
            return None
        course_id = input('程序序号：').strip()
        teacher_data = teacher_obj.cat_teacher()
        if teacher_data:
            for i,teacher_info in enumerate(teacher_data):
                print(i,teacher_info['teacher_name'],teacher_info['school_name'],teacher_info['addr'])
        else:
            func.echo('课程不存在，请先创建课程')
            return None
        teacher_id = input('讲师序号:').strip()
        class_name = input('班级名称：').strip()
        if class_name != '' and teacher_id != '' and course_id != '':
            res,msg = school_obj.create_class(class_name,course_id,teacher_id)
            func.echo(msg)
        else:
            func.echo('请添加准确的姓名')

    def create_course(self):
        '''
        创建课程
        :return:
        '''
        school_data = school_obj.cat_school()
        if school_data:
            for i,school_info in enumerate(school_data):
                print(i,school_info['addr'],school_info['school_name'])
        else:
            func.echo('请先创建学校')
            return None
        school = input('请输入校区数字').strip()
        cycle= input('课程周期：').strip()
        price =input('课程价格：').strip()
        name = input('课程名称').strip()
        if school != '' and cycle !='' and price != '' and name != '':
            data = {'course_name':name,'cycle':cycle,'price':price,'school_id':school}
            res,msg = course_obj.create_course(data)
            func.echo(msg)
        else:
            func.echo('课程需都添加')