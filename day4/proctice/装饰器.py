#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import time # 导入内置时间模块


login_status = {
    'user':None,
    'status':None
}


def login(user:str,pwd:str):
    if user == 'jmz' and pwd =='123':
        return True
    else:
        return False

# 认真用户是否登录成功
def auth(func):
    def wrapper(*args,**kwargs):
        if login_status['user'] and login_status['status']:
            return func(*args,**kwargs)
        else:
            uname = input('username>>').strip()
            upwd = input('password>>').strip()
            res =login(uname,upwd)
            if res:
                return func(*args, **kwargs)
            else:
                print('认证失败')
    return wrapper



def index():
    print('from index')

index = auth(index)

def cat():
    print('form cat')

index()
cat()