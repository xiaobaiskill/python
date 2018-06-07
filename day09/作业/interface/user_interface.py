#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib.common import encry
from db import db_handle
import os
from conf import settings

def add_user(user,pwd,data_size,home_dir):
    '''
    添加用户
    :param user:
    :param pwd:
    :param data_size:
    :param home_dir:
    :return:
    '''
    if db_handle.select(user,'user'):
        return False,'用户已存在，请勿重复操作'

    data = {}
    data['user'] = user
    data['pwd'] = encry(pwd)
    data['data_size'] = data_size
    data['home_dir'] = home_dir
    res = db_handle.save(data,'user')
    if res:
        ftp_user_dir = os.path.join(settings.FTP_DIR,user)
        if not os.path.isdir(ftp_user_dir):
            os.mkdir(ftp_user_dir)
        return True,'添加成功'
    else:
        return False,'添加失败'


def login(user,pwd):
    '''
    用户登陆接口
    :param user:
    :param pwd:
    :return:
    '''
    res = db_handle.select(user,'user')
    if res:
        if res['pwd'] == encry(pwd):
            return True,res
    return False,'用户名或密码错误'



