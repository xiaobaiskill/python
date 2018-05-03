#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz

from conf import config

if config.DB_INFO['type'] == 'mysql':
    from db.mysql import handle as type
else:
    from db.file import handle as type



def select(account):
    return type.select(account)

def update(account,data):
    return type.update(account,data)

def delete(account):

    return type.delete(account)

def insert(account,data):
    return type.insert(account,data)