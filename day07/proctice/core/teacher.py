#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from common import func

from models.classModel import classModel
from models.schoolModel import schoolModel
from models.teacherModel import teacherModel
from models.studentModel import studentModel
from models.scoreModel import scoreModel

classModel_obj = classModel()
teacherModel_obj =teacherModel()
schoolModel_obj = schoolModel()
studentModel_obj = studentModel()
scoreModel_obj = scoreModel()

class teacher:
    class_day = '01'
    def __init__(self):
        pass

    def class_management(self):
        '''
        班级管理
        :return:
        '''
        teacher_data = teacherModel_obj.cat_teacher()
        for k,teacher_info in enumerate(teacher_data):
            print('id:%s'%k,teacher_info)
        class_id = input('请选择班级序号：').strip()
        if class_id !='':
            self.class_id = class_id
            self.class_info = teacher_data[int(class_id)]
            self.student_management()
            return None
        else:
            func.echo('序号有误')
    def student_management(self):
        '''
        班级学生管理
        :return:
        '''
        class_manage = {
        '1':self.cat_student
        ,'2':self.record_in_class
        ,'3':self.make_score
        ,'4':self.cat_record_in_class
        ,'5':self.cat_score
        }

        while True:
            print('''
 ------欢迎来到班级管理------
    1.  查看学生
    2.  创建学员上课记录
    3.  创建学员成绩
    4.  查看学员上课记录
    5.  查看学员成绩
    q.  返回
            ''')
            select = input('请输入选项').strip()
            if select == 'q':
                return None
            elif select in class_manage:
                class_manage[select]()
    def cat_student(self):
        '''
        查看班级学生
        :return:
        '''
        data = studentModel_obj.cat_class_student(self.class_id)
        if data:
            func.echo('学生人数如下：')
            for info in data:
                func.echo('      %s'%info['student_name'])
            return None
        else:
            func.echo('暂无学员')

    def make_score(self):
        '''
        创建学员成绩
        :return:
        '''
        data = studentModel_obj.cat_class_student(self.class_id)
        for info in data:
            score = input('学生%s的成绩：'%info['student_name']).strip()
            score_info = {'student_name':info['student_name'],'class_id':self.class_id,'score':score,'class_day':self.class_day}
            scoreModel_obj.add_student(score_info)


    def record_in_class(self):
        '''
        上课记录
        :return:
        '''
        pass
    def cat_record_in_class(self):
        '''
        查看学员上课记录
        :return:
        '''
        pass

    def cat_score(self):
        '''
        查看学员成绩
        :return:
        '''
        data = scoreModel_obj.cat_class_id(self.class_id)
        if data:
            for info in data:
                func.echo('学员：%s,成绩：%s'%(info['student_name'],info['score']))
        else:
            func.echo('暂无学员成绩')
    def create_teacher(self):
        '''
        创建讲师
        :return:
        '''
        school_data = schoolModel_obj.cat_school()
        if school_data:
            for i, school_info in enumerate(school_data):
                print(i, school_info['addr'], school_info['school_name'])
        else:
            func.echo('请先创建学校')
            return None
        school_id = input('请输入校区数字').strip()
        name = input('讲师姓名：').strip()
        if school_id != '' and name != '':
            data = {'teacher_name':name,'school_id':school_id}
            res,msg=teacherModel_obj.create_teacher(data)
            func.echo(msg)
        else:
            func.echo('讲师信息需都添加')