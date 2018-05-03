#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 认证
DB_INFO ={
    'type':'file',
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}

# 日志记录
LOG_RECOED = {
    'account':'account.log',       # 流水日志记录文件
    'atm':'atm.log',                # atm 操作记录文件
    'path':"%s/log" % BASE_DIR
}

# 用户信息
LOGIN_USER ={
    'user':None,
    'pwd':None,
    'money':None,   # 卡的金额
    'cost':None,    # 已消费额度
    'status':False  # 状态
}

# 手续费
TRANSACTION_TYPE = {
    'pay':{ 'interest':0},                      # 支付
    'withdraw':{ 'interest':0.05},             # 提现
    'transfer_accounts':{ 'interest':0},      # 转账
}




