#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from common import func
from models.schoolModel import schoolModel
from models.courseModel import courseModel
from models.studentModel import studentModel
from models.scoreModel import scoreModel

schoolModel_obj = schoolModel()
courseModel_obj = courseModel()
studentModel_obj = studentModel()
scoreModel_obj =scoreModel()

class student:
    def __init__(self):
        pass
    def register(self):
        '''
            学员注册
        '''
        class_data = courseModel_obj.cat_course()
        if class_data:
            for i, course_info in enumerate(class_data):
                print('id：%s'%i, course_info)
        else:
            func.echo('请先创建学校')
            return None
        class_id = input('请选择班级id')
        student_name = input('name:').strip()
        res,msg = studentModel_obj.register(student_name,class_id)
        func.echo(msg)

    def login(self):
        '''
        学员登陆
        :return:
        '''
        student_name = input('请输入学生姓名：').strip()
        student_info = studentModel_obj.cat_student_name(student_name)
        if student_info:
            self.student_info=student_info
            self.student_handle()
            return None
        else:
            func.echo('不存在该学生')

    def student_handle(self):
        student_view = {
        '1':self.pay_edu
        # ,'2':self.record # 2.  查看上课记录
        ,'3':self.cat_score
        }
        while True:
            print('''
    ----- 欢迎进入学生页面
        1.  交学费
        
        3.  查看作业成绩
        q.  返回
            ''')
            select = input('你的选择').strip()
            if select == 'q':
                return None
            elif select in student_view:
                student_view[select]()
            else:
                func.echo('请输入正确的操作')

    def pay_edu(self):
        '''
        交学费
        :return:
        '''
        if 'pay_money' not in self.student_info:
            print('报名班级：%s,学校：%s,讲师：%s,学费：%s'%(
                self.student_info['class_name'],self.student_info['school_name'],self.student_info['teacher_name'],self.student_info['price']))
            pay_money = input('请输入缴费金额：').strip()
            res,msg=studentModel_obj.pay_money(self.student_info['student_name'],pay_money)
            func.echo(msg)
        else:
            func.echo('该学员已交过费用：%s'%self.student_info['pay_money'])



    def record(self):
        '''
        查看上课记录
        :return:
        '''
        pass
    def cat_score(self):
        '''
        查看成绩
        :return:
        '''
        data = scoreModel_obj.cat_student(self.student_info['student_name'])
        for info in data:
            func.echo('学员：%s,第%s天成绩：%s'%(self.student_info['student_name'],info['class_day'],info['score']))
        pass


if __name__ == '__main__':
    student_obj = student()
    student_obj.login()