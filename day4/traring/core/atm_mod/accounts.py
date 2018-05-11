#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import time
from conf import config
from core import common_func
from core import logger
from db import handle
from core.atm_mod import login

# 查看金额
@logger.logger('cat_money')
def cat_money():
    common_func.echo('卡号：%s,用户：%s,已消费金额：%s,剩余金额：%f'%(config.LOGIN_USER['account']
                                                     ,config.LOGIN_USER['user'],config.LOGIN_USER['cost']
                                                     ,float(config.LOGIN_USER['money'])))
    return True


# 提现
@logger.logger('withdraw')
def withdraw():
    money = input("请输入提现金额(or q退出)：").strip()
    if money =='q':
        return False
    elif money.replace('.','').isdigit():
        money = float(money)
        poundage = money * config.TRANSACTION_TYPE['withdraw']['interest']
        total = money + poundage
        if total < config.LOGIN_USER['money']:
            config.LOGIN_USER['cost'] = float(config.LOGIN_USER['cost']) + total
            config.LOGIN_USER['money'] = float(config.LOGIN_USER['money']) - total
            account_update_cost(config.LOGIN_USER['account'],'withdraw',money,poundage)
            return True
        else:
            common_func.echo('金额不足')
            return False
    else:
        common_func.echo('内容有误')
        return False

# 转账
@logger.logger('transfer_accounts')
def transfer_accounts():
    while True:
        account = input('account( or q exit):').strip()
        money = input('transfer money( or q exit):').strip()
        if account =='q' or money == 'q':
            return False
        account_user = handle.select(account)
        if not account_user:
            common_func.echo('转账用户不存在')
            continue
        is_money = money.replace('.','').isdigit()
        if account_user['account'] == config.LOGIN_USER['account']:
            common_func.echo('转账用户不能是自己')
            continue
        if is_money:
            amount = float(money)
            intersst = amount * config.TRANSACTION_TYPE['transfer_accounts']['interest']
            config.LOGIN_USER['cost'] = float(config.LOGIN_USER['cost']) + (amount + intersst)
            config.LOGIN_USER['money'] = float(config.LOGIN_USER['money']) - (amount + intersst)

            account_update_cost(config.LOGIN_USER['account'], 'transfer_accounts', amount, intersst)
            account_update_cost(account_user['account'], 'transfer_accounts', -amount, 0.0)
            common_func.echo('转账成功')
            return True
        else:
            common_func.echo('请输入正确的金额')
            continue

# 还款
@logger.logger('repayment')
def repayment():
    common_func.echo('您当前欠款 %s元'%config.LOGIN_USER['cost'])
    while True:
        amount = input('money repayment(or q exit):').strip()
        if amount == 'q':
            return False
        is_money = amount.replace('.','').isdigit()
        if is_money:
            amount = float(amount)
            intersst = amount * config.TRANSACTION_TYPE['repayment']['interest']
            config.LOGIN_USER['cost'] = float(config.LOGIN_USER['cost']) - (amount + intersst)
            config.LOGIN_USER['money'] = float(config.LOGIN_USER['money']) + (amount + intersst)
            account_update_cost(config.LOGIN_USER['account'], 'repayment', -amount, float(intersst))
            common_func.echo('还款成功')
            return True
        else:
            common_func.echo('请输入正确的金额')
            continue


# 现金变化 消费操作
def account_update_cost(account,action:str,amount:float,interest:float):
    '''
    :param account:账号
    :param money_float: 变动浮度
    :return:
    '''
    account_info = handle.select(account)
    account_info['cost'] = float(account_info['cost']) + amount + interest
    account_info['money'] = float(account_info['money']) - (amount + interest)
    logger.custom_record(account,action,-amount,interest)
    return handle.update(account, account_info)


# 支付
def pay(total:float):
    account_info = login.login()
    if account_info:
        money = total
        poundage = money * config.TRANSACTION_TYPE['pay']['interest']
        total = money + poundage
        if total < account_info['money']:
            account_update_cost(account_info['account'], 'pay', money, poundage)
            return True
        else:
            common_func.echo('金额不足')
            return False
    else:
        return False



