#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 1绑定方法
# 1.1绑定到对象
#     普通定义的类，调用是类内的函数都是绑定到对象的方法


# 1.2绑定到类
# classmethod

import settings
class Mysql(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port
    @classmethod
    def get_instast(cls):

        return cls(settings.HOST,settings.PORT)

conn = Mysql.get_instast()
print(conn.host)

# 2非绑定方法： 谁都可以调用的方法，和函数一样
# staticmethod
