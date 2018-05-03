#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import os,json
from conf import config
from core import common_func

# 认证
def auth(type='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            res = True
            if not config.LOGIN_USER['user']:
                account = input('account:').strip()
                pwd = input('password:').strip()
                if type == 'file':
                    res = file_auth(account,pwd)
                elif type == 'mysql':
                    res = sql_auth(account, pwd)
                else:
                    res = False
            if res:
                return func(*args,**kwargs)
        return wrapper
    return auth2


# 文件认证
def file_auth(account:str,pwd:str):
    auth_file = '%s/%s/%s.json' % (config.DB_INFO['path'], config.DB_INFO['name'], account)
    if os.path.isfile(auth_file):
        with open(auth_file, 'r', encoding='utf-8') as f:
            auth_info = json.load(f)
            if auth_info['pwd'] == pwd:
                if auth_info['status'] != '1':
                    common_func.echo('卡号冻结')
                    return False
                common_func.echo('登陆成功')
                config.LOGIN_USER = auth_info
                config.LOGIN_USER['account'] = account
                return True
    common_func.echo('用户名或密码错误')
    return False


# msyql 认证
def sql_auth(account:str,pwd:str):
    common_func.echo('sql认证暂不支持')
    return False