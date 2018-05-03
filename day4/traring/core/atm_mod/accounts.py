#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from conf import config
from core import common_func
from core import logger

# 查看金额
@logger.logger('cat_money')
def cat_money():
    common_func.echo('卡号：%s,用户：%s,已消费金额：%s,剩余金额：%f'%(config.LOGIN_USER['account']
                                                     ,config.LOGIN_USER['user'],config.LOGIN_USER['cost']
                                                     ,round((float(config.LOGIN_USER['money'])-float(config.LOGIN_USER['cost'])),4)))
    return True


# 提现
@logger.logger('withdraw')
def withdraw():
    money = input("请输入提现金额(or q退出)：").strip()
    if money =='q':
        return False
    elif money.strip('.').isdigit():
        money = float(money)
        poundage = money * config.TRANSACTION_TYPE['withdraw']['interest']
        total = money + poundage
        if total < config.LOGIN_USER['money']:

            logger.custom_record(config.LOGIN_USER['account'],'withdraw',money,poundage)
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
    pass

# 还款
@logger.logger('repayment')
def repayment():
    pass

# 支付
def pay():
    pass



