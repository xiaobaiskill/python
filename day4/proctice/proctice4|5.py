#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# proctice 四

db = 'db.txt'
login_dict = {'user':None,'status':False}

def auth(type='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            if login_dict['user'] and login_dict['status'] :
                return func(*args,**kwargs)
            if type == 'file':
                with open('db.txt',encoding='utf-8') as f:
                    dic = eval(f.read())
                    name = input('username:').strip()
                    pwd = input('password:').strip()
                    if name in dic.values() and pwd == dic['password']:
                        login_dict['user'] =name
                        login_dict['status'] = True
                        return func(*args,**kwargs)
                    else:
                        print('username or password error')
            elif type == 'sql':
                pass
            else:
                pass
        return wrapper
    return auth2


@auth()
def test():
    print('ok')

# test()


# proctice 五

import time
login_time={'user':None,'login_time':None,'timeout':0.01}

def auth_time(func):
    def wrapper(*args,**kwargs):
        if login_time['user']:
            if time.time() - login_time['login_time'] <login_time['timeout']:
                return func(*args,**kwargs)
        name = input('username:').strip()
        pwd = input('password:').strip()
        if name == 'jmz' and pwd =='123':
            login_time['user'] = name
            login_time['login_time'] = time.time()
            return func(*args,**kwargs)
    return wrapper

@auth_time
def index():
    print('index')

def home():
    print('home')


# index()
# home()
# time.sleep(1)
# index()