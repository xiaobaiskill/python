#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from db import db_handle

class base(object):
    @classmethod
    def get_info_by_name(cls,name):
        return db_handle.select(name,cls.__name__)



class manager(base):
    def __init__(self):
        pass
    def register(self,name,pwd):
        pass




if __name__ == '__main__':
    print(manager.get_info_by_name('jjj'))
