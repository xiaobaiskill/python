#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from models.schoolModel import schoolModel
from models.courseModel import courseModel
from models.teacherModel import teacherModel

schoolModel_obj = schoolModel()
courseModel_obj = courseModel()
teacherModel_obj = teacherModel()

class classModel():
    def __init__(self):
        pass
    def cat_class(self):
        '''
        查看班级信息
        :return:
        '''
        res = db_handle.select('class')
        if res:
            for k,class_info in enumerate(res):
                res[k].update(teacherModel_obj.cat_teacher_id(class_info['teacher_id']))
                res[k].update(courseModel_obj.cat_course_id(class_info['course_id']))
        else:
            return False
        return res
    def cat_class_id(self,id):
        res = db_handle.select('class')
        data = res[int(id)]

        data.update(teacherModel_obj.cat_teacher_id(data['teacher_id']))
        data.update(courseModel_obj.cat_course_id(data['course_id']))
        return data

    # def cat_class_tearcher(self):
    #     res = db_handle.select('class')
    #     print(res)
    #     pass



if __name__ == '__main__':
    class_obj = classModel()
    class_obj.cat_class_tearcher()