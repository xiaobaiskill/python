#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import random,os

from db import handle
from conf import config
from core import common_func

# 添加信用卡账号
def add_user():
    data = {
        'money': 15000,     # 信用金额
        'cost': '0',        # 已消费额度
        'status': '1'       # 状态
    }
    user = input('write user:').strip()
    pwd = input('write passwd:').strip()
    money = input('please input money(default 15000):').strip()
    if user and pwd:
        data['user'] = user
        data['pwd']  = pwd
        if money:
            data['money'] = money
        while True:
            account = random.randint(1000,9999)
            if not os.path.isfile('%s/%s.json'%(config.DB_INFO['path'],account)):
                if handle.insert(account,data):
                    common_func.echo('用户：%s,卡号:%s,信用卡金额：%s  信用卡申请成功'%(user,account,data['money']))
                    return True
                else:
                    common_func.echo('信用卡用户添加失败')
    else:
        common_func.echo('用户或密码不能为空')


# 添加信用额度
def add_money():
    account = input('write account:').strip()
    money = input('add money:').strip()
    account_info = handle.select(account)
    if account_info:
        is_money = money.replace('.','').isdigit()
        if is_money:
            account_info['money'] = float(account_info['money']) + float(money)
            handle.update(account,account_info)
            common_func.echo('卡号:%s,信用卡金额增加%s元，现%f元'%(account,money,account_info['money']))
        else:
            common_func.echo('请输入正确金额')
    else:
        common_func.echo('%s该信用卡不存在'%account)

# 减少信用额度
def dec_money():
    account = input('write account:').strip()
    money = input('dex money:').strip()
    account_info = handle.select(account)
    if account_info:
        is_money = money.replace('.','').isdigit()
        if is_money:
            account_info['money'] = float(account_info['money']) - float(money)
            handle.update(account,account_info)
            common_func.echo('卡号:%s,信用卡金额减少%s元，现%f元' % (account, money, account_info['money']))
        else:
            common_func.echo('请输入正确金额')
    else:
        common_func.echo('%s该信用卡不存在'%account)

# 冻结账号
def fork_user():
    account = input('account:').strip()
    if handle.update_status(account,'0'):
        common_func.echo('用户已冻结')
    else:
        common_func.echo('冻结失败')

# 解冻账号
def unfork_user():
    account = input('account:').strip()
    if handle.update_status(account,'1'):
        common_func.echo('用户已解冻')
    else:
        common_func.echo('解冻失败')




