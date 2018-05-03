#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import time,os
from conf import config
from core import common_func

# atm 操作记录--装饰器
def logger(action):
    # 2018-05-02 14:21:34 atm - INFO - account:1234  action:type
    def account(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if res:
                content = '%s atm - INFO - account:%s  action:%s' % (
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), config.LOGIN_USER['account'], action)
                log_record(content, '%s/%s.%s' % (
                config.LOG_RECOED['path'], config.LOGIN_USER['account'], config.LOG_RECOED['atm']))
            return res
        return wrapper
    return account


# 消费流水记录
def custom_record(account,action:str,amount:float,interest:float):
    '''
    消费流水记录
    :param account: 卡号
    :param action: 操作
    :param amount: 金额
    :param interest: 手续费
    :return:
    '''
    # 2018-05-02 14:21:34,840 - transaction - INFO - account:1234   action:repay    amount:600.0   interest:0.0
    content = '%s account - INFO - account:%s  action:%s  amount:%s  intersst:%f' % (
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), account, action,amount,interest)
    log_record(content, '%s/%s.%s' % (
                config.LOG_RECOED['path'], account, config.LOG_RECOED['account']))
    return True

# 日志记录
def log_record(context:str,file):
    with open(file,'a',encoding='utf-8') as f:
        f.write('%s\n'%context)
    pass


# 查看atm操作日志
@logger('cat_atm_log')
def cat_atm_log():
    file = '%s/%s.%s'%(config.LOG_RECOED['path'],config.LOGIN_USER['account'],config.LOG_RECOED['atm'])
    if os.path.isfile(file):
        with open(file,'r',encoding='utf-8') as f:
            for line in f:
                common_func.echo(line.strip())
        return True
    else:
        common_func.echo('暂无信息')
        return False

# 查看消费流水
@logger('cat_account_log')
def cat_account_log():
    file = '%s/%s.%s'%(config.LOG_RECOED['path'],config.LOGIN_USER['account'],config.LOG_RECOED['account'])
    if os.path.isfile(file):
        with open(file,'r',encoding='utf-8') as f:
            for line in f:
                common_func.echo(line.strip())
        return True
    else:
        common_func.echo('暂无信息')
        return False

