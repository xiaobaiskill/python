#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from models.classModel import classModel
classModel_obj = classModel()

class studentModel:
    def __init__(self):
        pass
    def register(self,name,class_id):
        data = {'student_name':name,'class_id':class_id,'pay_edu':0}
        res = db_handle.add('student',data)
        if res:
            return True,'学员创建成功'
        else:
            return False,'学员创建失败'
    def cat_student_name(self,name):
        '''
            获取学生班级信息
        :param name:
        :return:
        '''
        res = db_handle.select('student')
        for student_info in res:
            if name in student_info.values():
                student_info.update(classModel_obj.cat_class_id(student_info['class_id']))
                return student_info
    def cat_class_student(self,class_id):
        '''
        查看班级下的学生数
        :return:
        '''
        res = db_handle.select('student')
        data = []
        for student_info in res:
            if student_info['class_id'] == str(class_id):
                data.append(student_info)
        return data

    def pay_money(self,name,money):
        res = db_handle.select('student')
        data =[]
        is_member= False
        for info in res:
            if name in info.values():
                info['pay_money'] = money
                is_member = True
            data.append(info)
        res = db_handle.save('student', data)
        if res and is_member:
            return True,'学费缴成功'
        else:
            return False,'学费没有缴成功'




if __name__ == '__main__':
    student_obj = studentModel()
    data = student_obj.cat_class_student()
    print(data)