#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from conf import settings
import os,json

def save(data,table):
    table_dir = os.path.join(settings.DB_DIR,table)
    if not os.path.isdir(table_dir):
        os.mkdir(table_dir)
    user_table = os.path.join(table_dir,'%s.db'%data['user'])
    with open(user_table,'w',encoding='utf-8') as f:
        json.dump(data,f)
        f.flush()
    return True

def select(user,table):
    user_table = os.path.join(settings.DB_DIR,table,'%s.db'%user)
    if os.path.exists(user_table):
        with open(user_table,'r',encoding='utf-8') as f:
            return json.load(f)

if __name__ == '__main__':
    # print(select('root','root'))
    from lib.common import encry
    data = {
        'user':'root',
        'pwd':encry('root')
    }
    save(data,'admin')





