#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from lib.common import hash_md5

def find(name):
    data = db_handle.select('member',name)
    return data

def register(user,passwd):
    data = {}
    user = user.encode('utf-8')
    if find(user):
        return False,'用户已经存在'
    data['user'] = user
    data['passwd'] = hash_md5(passwd)
    db_handle.save('membber',user,data)
    return True,'注册成功'

def login(name,passwd):
    pass





