#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle


class base(object):
    @classmethod
    def get_info_by_name(cls,name):
        return db_handle.select(name,cls.__name__)

    def save(self):
        return db_handle.save(self)

# 管理者
class manager(base):
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.save()
    def register(self,name,pwd):
        pass

# 学校
class school(base):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.course_list = []
        self.teacher_list = []
        self.save()
    def add_teacher(self,teacher_name):
        self.teacher_list.append(teacher_name)
        self.save()
    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()

# 老师
class teacher(base):
    def __init__(self,name,pwd,school_name):
        self.name = name
        self.pwd = pwd
        self.school_name = school_name
        self.course_list = []
        self.save()
    def add_course(self,course_name):
        if course_name in self.course_list:
            return False,'课程已存在'
        else:
            self.course_list.append(course_name)
            self.save()
            return True,'添加成功'



# 课程
class course(base):
    def __init__(self,name):
        self.name = name
        self.teacher_name = ''
        self.student_list = []
        self.save()
    def add_student(self,student_name):
        self.student_list.append(student_name)
        return self.save()
    def add_teacher(self,teacher_name):
        self.teacher_name = teacher_name
        self.save()




# 学生
class student(base):
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.course_list = []
        self.school_name = ''
        self.score = {}
        self.save()

    def add_school(self,school_name):
        if not self.school_name:
            self.school_name = school_name
            return self.save()
        else:
            return False
    def add_course(self,course_name):
        if course_name in self.course_list:
            return False
        else:
            self.course_list.append(course_name)
            self.save()
            return True
    def add_score(self,course_name,score):
        self.score[course_name] = score
        self.save()
        return True






if __name__ == '__main__':
    print(student.get_info_by_name('jmz'))
