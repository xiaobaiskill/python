#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

#user数据类型：     id,用户名,密码,状态,金额

import os
LOGIN_SUCCESS=[]   # 多账号使用
CURRENT_USER=''    # 当前账号使用
POUNDAGE = 0.05    # 提现汇率


def echo_red(context):
    '''
    打印红色字
    :param context:
    :return:
    '''
    print('\033[5;31;m%s\033[0m'%(context))

def register():
    '''
    注册信息 函数
    :return: boolean
    '''
    while True:
        user = input('please input username:').strip()
        if not user:
            echo_red('用户名不能为空')
            continue
        if not get_user(user):
            pwd = input('please input password:').strip()
            confirm_pwd = input('please input confirm password:').strip()
            if not pwd:
                echo_red('密码不能为空')
                continue
            if pwd == confirm_pwd:
                echo_red('请输入你的金额，默认为15000')
                money = input('your money:').strip()
                if money and not money.replace('.','',1).isdecimal():
                    echo_red('请输入正确的金额')
                else:
                    money = 15000 if not money else float(money)
                    if add_user(user,pwd,money):
                        echo_red('恭喜 %s 注册成功'%user)
                        global CURRENT_USER,LOGIN_SUCCESS
                        LOGIN_SUCCESS.append(user)
                        CURRENT_USER=user
                        return True
            else:
                echo_red('两次密码不一致')
        else:
            echo_red('用户名以存在')
            continue


def get_user(user):
    '''
    确认是否已存在用户
    :param user: 用户名
    :return:  存在 返回信息 不存在返回false
    '''
    with open('user','r',encoding='utf-8') as f:
        for line in f:
            if line.strip():
                new_list = line.strip().split(',')
                user_info = {
                    'id':new_list[0]
                    ,'user':new_list[1]
                    ,'pwd':new_list[2]
                    ,'status':new_list[3]
                    ,'money':new_list[4]
                }
                if user_info['user'] == user:
                    return user_info
    return False


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
            if line.strip():
                new_list=line.split(',')
                max_id = int(new_list[0]) if int(new_list[0]) >max_id else max_id
    with open('user','a',encoding='utf-8') as f_a:
        f_a.write('%d,%s,%s,%d,%s\n'%(max_id+1,user,pwd,1,str(money)))

    return True


def input_login():
    '''
    输入登陆
    :return: boolean
    '''
    while True:
        user = input('please input username:').strip()
        if user in LOGIN_SUCCESS:
            echo_red('用户已登陆')
            continue
        pwd = input('please input password:').strip()
        res = login(user,pwd)
        if res:
            if res == '-1':
                echo_red('用户锁定')
                return False
            else:
                echo_red('%s 登陆成功' % user)
                return True
        else:
            echo_red('username or password error')

def login(user,pwd):
    '''
    验证登陆
    :param user: 用户名
    :param pwd: 密码
    :return: boolean
    '''
    with open('user','r',encoding='utf-8') as f_user:
        for line in f_user:
            if line.strip():
                user_list = line.strip().split(',')
                if user == user_list[1] and pwd ==user_list[2]:
                    if user_list[3] == '1':
                        global CURRENT_USER,LOGIN_SUCCESS
                        CURRENT_USER = user
                        LOGIN_SUCCESS.append(user)
                        return True
                    else:
                        return '-1'
    return False

def cat_login():
    global CURRENT_USER,LOGIN_SUCCESS
    echo_red('当前账号为:%s, 当前已登录账号:%s'%(CURRENT_USER,','.join(LOGIN_SUCCESS)))

def login_cut():
    '''
    账号切换
    :return: boolean
    '''
    user = input('please input cut username:').strip()
    if user:
        if user in LOGIN_SUCCESS:
            global CURRENT_USER
            CURRENT_USER = user
            echo_red('切换成功')
            return True
        else:
            echo_red('未登陆该用户')
            return False
    echo_red('用户名为空，未切换')
    return False

def tixian():

    money = input('Please enter the present amount:').strip()
    if money.replace('.','',1).isdigit():
        global POUNDAGE, CURRENT_USER
        poundage = round(float(money) * POUNDAGE, 2)
        total = poundage + float(money)
        user_info = get_user(CURRENT_USER)
        if total <= float(user_info['money']):
            reduce_moeny(CURRENT_USER,total)
            echo_red('提现成功 提现金额：%s, 手续费：%s'%(str(money),str(poundage)))
            return True
        else:
            echo_red('金额不足')
            return False
    else:
        echo_red('不合法的金额')
        return False

def cat_money():
    '''
    查看余额
    :return:
    '''
    user_info = get_user(CURRENT_USER)
    echo_red('当前用户%s 余额 %s '%(user_info['user'],user_info['money']))
    return True

def ts_money():
    '''
    转账
    :return:
    '''
    exit = False
    while not exit:
        user = input('Please enter the transfer user(q to exit)').strip()
        if user == 'q':
            break
        elif user == CURRENT_USER:
            echo_red('connot transfer to your')
        elif user:
            user_info = get_user(user)
            if user_info:
                if user_info['status'] != '1':
                    echo_red('%s 用户已锁定，无法转账'%(user))
                else:
                    while not exit:
                        money = input('Please enter the amount of the transfer(q to exit)').strip()
                        if money == 'q':
                            break
                        if money.replace('.','',1).isdigit():
                            money = float(money)
                            user_info = get_user(CURRENT_USER)
                            if money < float(user_info['money']):
                                add_money(user,money)
                                reduce_moeny(CURRENT_USER,money)
                                echo_red('转账成功')
                                exit= True
                            else:
                                echo_red('您的金额不足，无法转账')
                        else:
                            echo_red('金额输入有误')
            else:
                echo_red('用户不存在')

def add_money(user:str,money:float):
    '''
    添加金额
    :param user:
    :param money:
    :return:
    '''
    user_info = get_user(user)
    if user_info:
        if user_info['status'] == '1':
            user_info['money'] = str(round(float(user_info['money']) + money,2))
            update_user(user,user_info)
            return True
        else:
            return False
    else:
        return False

def reduce_moeny(user:str,money:float):
    '''
        减少金额
        :param user:
        :param money:
        :return:
        '''
    user_info = get_user(user)
    if user_info:
        if user_info['status'] == '1':
            user_info['money'] = str(round(float(user_info['money']) - money,2))
            update_user(user, user_info)
            return True
        else:
            return False
    else:
        return False

def update_user(user:str,user_info):
    '''
    修改用户的信息
    :param user: 用户名
    :param user_info: 新的用户信息
    :return:
    '''
    with open('user','r',encoding='utf-8') as f_user,open('user.swap','a',encoding='utf-8') as f_new:
        for line in f_user:
            line = line.strip()
            if line:
                user_list = line.split(',')
                if user_list[1] == user:
                    user_info = '%s,%s,%s,%s,%s'%(user_info['id'],user,user_info['pwd'],user_info['status'],user_info['money'])
                    f_new.write('%s\n'%user_info)
                    continue
            f_new.write('%s\n'%line)
    os.remove('user')
    os.rename('user.swap','user')

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
    ,['登录',input_login]
]

# 登陆注册操作
while True:
    for value in enumerate(reg_or_login):
        print(value[0]+1,value[1][0])
    chooise = input('chooise>>').strip()

    if chooise.isdecimal():
        chooise_int = int(chooise)
        if chooise_int <= len(reg_or_login):
            if reg_or_login[chooise_int-1][1]():
                break
    print('请输入正确的指令')



# 登陆后的操作
menu = [
    ['登陆新的账号',input_login]
    ,['查看当前登录账号',cat_login]
    ,['账号切换',login_cut]
    ,['查看余额',cat_money]
    ,['转账',ts_money]
    ,['提现',tixian]
]

while True:
    k =1
    for value in menu:
        print(k,value[0])
        k+=1
    print('q','退出')
    chooise = input('chooise>>').strip()
    if chooise =='q':
        break
    elif chooise.isdigit():
        if int(chooise) <= len(menu):
            menu[int(chooise)-1][1]()
    else:
        print('请输入正确的指令')
