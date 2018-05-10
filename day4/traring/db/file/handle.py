#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz

import os,json
from conf import config

file_dir = '%s/%s'%(config.DB_INFO['path'],config.DB_INFO['name'])

def select(account):
    if os.path.isfile('%s/%s.json'%(file_dir,account)):
        with open('%s/%s.json'%(file_dir,account),'r',encoding='utf-8') as f:
            res = json.load(f)
            res['account'] = account
            return res
    return False

def update(account,data):
    with open('%s/%s.json' % (file_dir, account), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))
    return True

def delete(account):
    os.remove('%s/%s.json'%(file_dir,account))
    return True

def insert(account,data):
    with open('%s/%s.json' % (file_dir, account), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))
    return True

def update_info(account,data):
    user_info = select(account)
    if user_info:
        user_info.update(data)
        return update(account,user_info)
    else:
        return False

