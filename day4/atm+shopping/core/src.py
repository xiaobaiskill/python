#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



def atm():
    while True:
        print('''
----请输入您的操作---
    1、注册
    2、登录
    3、查看金额
    4、转账
    5、提现
    6、查看操作日志
    7、查看流水
    8、还款        
        ''')
    pass


def shopping():
    while True:
        print('''
------请输入您的操作---
    1、购物操作
    2、查看添加的商品
    3、购买        
        
        ''')




def auth(func):
    def wrap(*args, **kwargs):
        user = input('>>>').strip()
        pwd = input('>>>').strip()

        pass

    return wrap








