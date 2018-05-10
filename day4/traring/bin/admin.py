#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import common_func
from conf import config
from core import admin

ADMIN_INFO = {'user':None,'pwd':None}

def login(func):
    def wrapper(*args,**kwargs):
        global ADMIN_INFO
        count = 0
        while count < 3:
            if not ADMIN_INFO['user']:
                user = input('admin:').strip()
                pwd = input('password:').strip()
                with open('%s/%s/%s.json'%(config.BASE_DIR,'db/admin','admin'),'r',encoding='utf-8') as f:
                    res = json.load(f)
                if res['user'] == user and pwd == res['pwd'] and res['status'] !=1:
                    ADMIN_INFO = res
                    return func(*args,**kwargs)
                else:
                    common_func.echo('用户名名或密码错误或管理账号冻结')
                    count +=1
                    continue
            else:
                return func(*args, **kwargs)
        else:
            common_func.echo('输入次数过多，退出程序')
    return wrapper

admin_chooise = [
    ['添加账号',admin.add_user],
    ['增加信用卡额度',admin.add_money],
    ['减少增加信用卡额度',admin.dec_money],
    ['冻结账号',admin.fork_user],
    ['解冻账号',admin.unfork_user]
]

@login
def run():
    while True:
        k =0
        for v in admin_chooise:
            print(k,v[0])
            k+=1
        chooise = input('请输入你的选择(q 退出):').strip()
        if chooise.isdigit() and int(chooise) < k:
            admin_chooise[int(chooise)][1]()
        elif chooise == 'q':
            break
        elif chooise:
            common_func.echo('请输入正确的指令')

run()







