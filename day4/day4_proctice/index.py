#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

def register():
    while True:
        user = input('please input username:').strip()
        if not user:
            print('用户名不能为空')
            continue
        if confirm_user(user):
            pwd = input('please input password:').strip()
            confirm_pwd = input('please input confirm password:').strip()
            if not pwd:
                print('密码不能为空')
                continue
            if pwd == confirm_pwd:
                print('请输入你的金额，默认为15000')
                money = input('your money:').strip()
                if money and not money.isdecimal():
                    print('请输入正确的金额')
                else:
                    money = 1500 if not money else int(money)
                    if add_user(user,pwd,int(money)):
                        print('注册成功')
                        break
            else:
                print('两次密码不一致')

        else:
            print('用户名以存在')
            continue

#id,用户名,密码,状态,金额
def confirm_user(user):
    with open('user','r',encoding='utf-8') as f:
        for line in f:
            new_list = line.split(',')
            if new_list[1] == user:
                return False

    return True

def add_user(user,pwd,money=15000):
    '''
    添加新的用户
    :param user:
    :param pwd:
    :param money:
    :return:
    '''
    with open('user','r',encoding='utf-8') as f:
        max_id =0
        for line in f:
            new_list=line.split(',')
            max_id = int(new_list[0]) if int(new_list[0]) >max_id else max_id
    with open('user','a',encoding='utf-8') as f_a:
        f_a.write('%d,%s,%s,%d,%d\n'%(max_id,user,pwd,1,int(money)))

    return True

def login():
    pass

def tixian():
    pass

def moeny():
    '''
    查看余额
    :return:
    '''
    pass

def ts_money():
    '''
    转账
    :return:
    '''
    pass


def cat_log():
    '''
    查看日志
    :return:
    '''
    pass

def log():
    '''
    记录日志
    :return:
    '''
    pass



reg_or_login= [
    ['注册',register]
    ,['登录',login]
]

while True:
    for value in enumerate(reg_or_login):
        print(value[0]+1,value[1][0])
    chooise = input('chooise>>').strip()

    if chooise.isdecimal():
        chooise_int = int(chooise)
        if chooise_int <= len(reg_or_login):
            reg_or_login[chooise_int-1][1]()
    print('请输入正确的指令')







#
# menu = [
#     ['查看余额',moeny]
#     ,['转账',ts_money]
#     ,['提现',tixian]
# ]

