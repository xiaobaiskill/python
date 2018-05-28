#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import pickle,os
from config.setting import DB_DIR  

def add(name,data):
    '''
    保存数据
    :param name:
    :param date: {}
    :param table:
    :return:
    '''
    get_data = select(name)
    if get_data:
        get_data.append(data)
        data = get_data
    else:
        data = [data]
    with open('%s/%s.pick'%(DB_DIR,name),'wb') as f:
        pickle.dump(data,f)
    return True

def save(name,data):
    '''
    修改后直接保存
    :param name:
    :param data:
    :return:
    '''
    with open('%s/%s.pick' % (DB_DIR, name), 'wb') as f:
        pickle.dump(data,f)
    return True


def select(name):
    '''
    查看数据
    :param name:
    :param table:
    :return:
    '''
    if os.path.isfile('%s/%s.pick'%(DB_DIR,name)):
        with open('%s/%s.pick'%(DB_DIR,name),'rb') as f:
            return pickle.load(f)
    
    
if __name__ == '__main__':
    print(select('class'))