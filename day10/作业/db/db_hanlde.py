#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os,configparser
from conf import settings

conf = configparser.ConfigParser()
# 查找
def select(name,key = None):
    try:
        if key:
            conf.read(settings.DB_HOSTS_FILE)
            return conf.get(name,key)
        else:
            return conf.options()
    except Exception as e:
        return None

# 修改
def save(name,data):
    if not os.path.exists(settings.DB_HOSTS_DIR):
        os.mkdir(settings.DB_HOSTS_DIR)

    if isinstance(data,dict):
        conf = configparser.ConfigParser()
        try:
            name = data['name']
            conf.add_section(name)
            data.pop('name')
            for k in data:
                conf.set(name,k,str(data[k]))
            conf.write(open(settings.DB_HOSTS_FILE,'w'))
            return True
        except Exception:
            return False
    else:
        return False


# 添加
def add(data):
    if not os.path.exists(settings.DB_HOSTS_DIR):
        os.mkdir(settings.DB_HOSTS_DIR)
    if isinstance(data, dict):
        conf.read(settings.DB_HOSTS_FILE,encoding=settings.DB_CHAR)
        try:
            name = data['name']
            conf.add_section(name)
            data.pop('name')
            for k in data:
                conf.set(name,k,str(data[k]))
            conf.write(open(settings.DB_HOSTS_FILE,'w'))
            return True
        except Exception:
            return False
    else:
        return False

# 删
def remove(name,key = None):
    conf.read(settings.DB_HOSTS_FILE,encoding=settings.DB_CHAR)

    if key:
        if conf.has_option(name,key):
            conf.remove_option(name, key)
    else:
        if conf.has_section(name):
            conf.remove_section(name)
    return True

if __name__ == '__main__':
    # print(select('jmz'))
    # data = {
    #     'name':'jmz111',
    #     'ip':'192.168.33.110',
    #     'port':22,
    #     'username':'vagrant',
    #     'passwd':'vagrant',
    #     'private_key':'none'
    # }
    # add(data)

    # data = {
    #     'name':
    # }
    conf.read(settings.DB_HOSTS_FILE)
    print(conf.sections())


