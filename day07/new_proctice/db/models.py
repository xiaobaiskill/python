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
        self.save()

# 老师
class teacher(base):
    pass


# 课程
class course(base):
    pass



# 学生
class student(base):
    pass






if __name__ == '__main__':
    print(manager.get_info_by_name('jjj'))
