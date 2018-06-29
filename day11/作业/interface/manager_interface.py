#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from lib.common import hash_md5

def find(name):
    data = db_handle.select('manager',name)
    return data

def register(user,passwd):
    data = {}
    if find(user):
        return False,'用户已经存在'
    data['user'] = user
    data['passwd'] = hash_md5(passwd)
    db_handle.save('manager',user,data)
    return True,'注册成功'

def login(name,passwd):
    data = find(name)
    if not data:
        return False,'用户不存在'
    if data[0]['passwd'] == hash_md5(passwd):
        return True,data[0]
    else:
        return False,'用户名或密码有误'





