#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



from conf import config
from core import common_func
from db import handle

# 认证
def auth(type='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            res = True
            if not config.LOGIN_USER['user']:
                account = input('account:').strip()
                pwd = input('password:').strip()
                res = auth_handle(account,pwd)
            if res:
                return func(*args,**kwargs)
        return wrapper
    return auth2


# 文件认证
def auth_handle(account:str,pwd:str):
    res = handle.select(account)
    if res and res['pwd'] == pwd:
        if res['status'] != '1':
            common_func.echo('卡号已被冻结')
            return False
        else:
            common_func.echo('登陆成功')
            config.LOGIN_USER = res
            config.LOGIN_USER['account'] = account
            return True
    else:
        common_func.echo('用户名或密码错误')
        return False

