#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



from db import handle
from core import common_func

def login():
    account = input('account(q 退出):').strip()
    pwd = input('password:').strip()
    res = handle.select(account)
    if account =='q':
        return False
    if res and res['pwd'] == pwd:
        if res['status'] != '1':
            common_func.echo('卡号冻结')
            return False
        else:
            res['account'] = account
            return res
    else:
        common_func.echo('用户名或密码错误')
        return False


