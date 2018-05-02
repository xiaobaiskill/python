#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from core import atm
from core import shopping
from core import login
from core import accounts
from core import logger

CHOOISE_ADDRESS = [
    ['银行',atm.run],
    ['购物商场',shopping.run]
]

ATM_CHOOISE = [
    ['登录',login.login],
    ['提现',accounts.tixian],
    ['转账',accounts.ts_moeny],
    ['查看消费流水',logger.cat_custom],
    ['查看atm 操作记录',logger.cat_atm_log]
]

LOGIN_STATUS ={
    'user':None,
    'money':None,
    'cost':None,
    'status':False
}





