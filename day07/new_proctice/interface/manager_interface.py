#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from db import models


def register(name,pwd):
    if not models.manager.get_info_by_name(name):
        models.manager(name,pwd)
        return True,'管理用户注册成功'
    else:
        return False,'管理用户已存在'

def login(name,pwd):
    data = models.manager.get_info_by_name(name)
    if data:
        if data.pwd == pwd: return True,'登陆成功'
    else:
        return False,'用户名或密码错误'





def create_course():
    pass