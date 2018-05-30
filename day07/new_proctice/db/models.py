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
    def __init__(self,name,school_name):
        self.name = name
        self.school_name = school_name
        self.save()
    pass


# 课程
class course(base):
    def __init__(self,name):
        self.name = name
        self.save()




# 学生
class student(base):
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.save()






if __name__ == '__main__':
    print(manager.get_info_by_name('jjj'))
