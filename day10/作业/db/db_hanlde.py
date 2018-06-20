#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os,configparser
from conf import settings

conf = configparser.ConfigParser()
# 查找
def select(name=None,key = None):
        conf.read(settings.DB_HOSTS_FILE, encoding=settings.DB_CHAR)
        try:
            if key:
                return conf.get(name,key)
            elif name:
                return conf.options(name)
            else:
                return conf.sections()
        except Exception:
            return None

# 修改
def save(name,data):
    if not os.path.exists(settings.DB_HOSTS_DIR):
        os.mkdir(settings.DB_HOSTS_DIR)

    if isinstance(data,dict):
        try:
            conf.read(settings.DB_HOSTS_FILE,encoding=settings.DB_CHAR)
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

    conf.write(open(settings.DB_HOSTS_FILE,'w'))
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
    #     'ip':'123.33.33.33',
    #     'port':51622,
    #     'username':'root'
    # }
    # save('jmz',data)


    # remove('jmz','ip')

    print(select())
    #
    # conf.read(settings.DB_HOSTS_FILE,encoding=settings.DB_CHAR)
    # print(conf.sections())
    # print(conf.options('jmz'))
    # print(conf.get('jmz','ip'))


