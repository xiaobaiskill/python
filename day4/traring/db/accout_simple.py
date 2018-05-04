#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz

import json
account ={
    'user':'jmz',
    'pwd':'123',
    'money':15000,  # 信用金额
    'cost':'0',    # 已消费额度
    'status':'1'  # 状态
}
with open('accounts/1234.json','w',encoding='utf-8') as f:
    f.write(json.dumps(account))

# with open('accounts/1234.json','r',encoding='utf-8') as f:
#     res = json.load(f)
#     print(res,type(res))

