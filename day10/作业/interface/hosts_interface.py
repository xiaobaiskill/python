#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_hanlde

def add(name,ip,port=None,user=None,pwd=None,keyfile=None):
    data = {
        'name':name,
        'ip':ip,
        'port':port,
        'user':user,
        'pwd':pwd,
        'keyfile':keyfile,
    }
    res = db_hanlde.add(data)
    if res:
        msg = '添加成功'
    else:
        msg = '数据添加失败'
    return res,msg

def cat_one(name=None,key=None):
    return db_hanlde.select(name,key)


# 查看所有的主机信息
def cat_all():
    data = {}
    for k in cat_one():
        res = cat_one(k)
        info ={}
        for kk in res:
            info[kk] =cat_one(k,kk)
        data[k] = info
    return data


def remove(name,key = None):
    res = db_hanlde.remove(name,key)
    if res:
        msg = '删除成功'
    else:
        msg = '数据删除失败'
    return res,msg


def save(name,ip,port=None,user=None,pwd=None,keyfile=None):
    data = {
        'ip':ip,
        'port':port,
        'user':user,
        'pwd':pwd,
        'keyfile':keyfile,
    }
    res = db_hanlde.save(name,data)
    if res:
        msg = '修改成功'
    else:
        msg = '数据修改失败'
    return res,msg



if __name__ == '__main__':
    print(cat_all())
