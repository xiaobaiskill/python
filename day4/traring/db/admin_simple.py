#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz

import json
account ={
    'user':'adin',
    'pwd' :'123',
    'status':'1'  # 状态
}
with open('admin/admin.json','w',encoding='utf-8') as f:
    f.write(json.dumps(account))

# with open('accounts/1234.json','r',encoding='utf-8') as f:
#     res = json.load(f)
#     print(res,type(res))

