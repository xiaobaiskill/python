#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from conf import settings
import os,json

def select(table,name=None):
    db_table = '%s/%s'%(settings.DB_DIR,table)
    if not os.path.exists(db_table):
        os.mkdir(db_table)
    data = []
    if name is None:
        for file in os.listdir(db_table):
            with open('%s/%s'%(db_table,file),'r',encoding=settings.CHAR) as f:
                data.append(json.load(f))
    else:
        if os.path.isfile('%s/%s.json'%(db_table,name)):
            with open('%s/%s.json'%(db_table,name),'r',encoding=settings.CHAR) as f:
                data.append(json.load(f))
    return data

def save(table,name,data):
    db_table = '%s/%s' % (settings.DB_DIR, table)
    if not os.path.exists(db_table):
        os.mkdir(db_table)
    with open('%s/%s.json'%(db_table,name),'w',encoding=settings.CHAR) as f:
        json.dump(data,f)
    return True


if __name__ == '__main__':
    # save('admin','jj',{'name':'jjj','age':123})
    # print(select('admin','jj'))
    pass




