#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import models

def register(name,pwd):
    if models.student.get_info_by_name(name):
        return False,'学员已存在'
    else:
        models.student(name,pwd)
        return True,'学员注册成功'

def login(name,pwd):
    student_data = models.student.get_info_by_name(name)
    if student_data.pwd == pwd:
        return True,'登录成功'
    else:
        return False,'用户名或密码不一致'