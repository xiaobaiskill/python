#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from core import auth
from conf import config
from core.atm_mod import login
from core.atm_mod import accounts
from core import logger

import core.logger as logger
import core.common_func as common_func

atm_chooise = [
    ['登录',login.login],
    ['提现',accounts.withdraw],
    ['转账',accounts.transfer_accounts],
    ['查看金额',accounts.cat_money],
    ['查看消费流水',logger.cat_account_log],
    ['查看atm操作记录',logger.cat_atm_log]
]

@auth.auth(config.AUTH_INFO['type'])
def run():
    while True:
        k =0
        for v in atm_chooise:
            print(k,v[0])
            k+=1
        chooise = input('请输入你的选择:').strip()
        if chooise.isdigit() and int(chooise) < k:
            atm_chooise[int(chooise)][1]()
        elif chooise == 'q':
            break
        elif chooise:
            common_func.echo('请输入正确的指令')


