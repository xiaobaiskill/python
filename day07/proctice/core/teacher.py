#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from interface import school
from common import func

from interface.school import school as school_obj
from interface.teacher import teacher as teacher_obj

teacher_obj =teacher_obj()
school_obj = school_obj()


class teacher:
    def __init__(self):
        pass

    def record_in_class(self):
        '''
        上课记录
        :return:
        '''
        pass
    def make_score(self):
        '''
        创建学员成绩
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
        pass
    def create_teacher(self):
        '''
        创建讲师
        :return:
        '''
        school_data = school_obj.cat_school()
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
            res,msg=teacher_obj.create_teacher(data)
            func.echo(msg)
        else:
            func.echo('讲师信息需都添加')