#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from lib.common import hash_md5

def find(name=None):
    data = db_handle.select('member',name)
    return data

def register(user,passwd):
    data = {}
    if find(user):
        return False,'用户已经存在'
    data['user'] = user
    data['passwd'] = hash_md5(passwd)
    data['level'] = 0
    data['lock'] = 0
    db_handle.save('member',user,data)
    return True,'注册成功'

def login(name,passwd):
    data = find(name)
    if not data:
        return False,'用户不存在'
    if data[0]['lock'] == 1:return False,'用户已锁'
    if data[0]['passwd'] == hash_md5(passwd):
        return True,data[0]
    else:
        return False,'用户名或密码有误'



def buy_vip(name,money):
    data = find(name)
    if not data:
        return False,'用户不存在'
    info = data[0]
    info['level'] = 1
    db_handle.save('member',name,info)
    return True,'会员充值成功'


def member_lock(name,lock = 0):
    '''
    锁定解锁用户
    :param name:
    :param lock:
    :return:
    '''
    data = find(name)
    if not data:
        return False,'用户不存在'
    info = data[0]
    info['lock'] = lock
    db_handle.save('member',name,info)
    return True,'设置成功'

