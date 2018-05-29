#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from config import setting
import pickle,os


def save(obj):
    path = '%s/%s'%(setting.BASE_DIR,obj.__class__.__name__)
    if not os.path.isdir(path):
        os.mkdir(path)
    with open('%s/%s'%(path,obj.name),'wb') as f:
        pickle.dump(obj,f)
    return True




def select(name,type):
    path = '%s/%s/%s'%(setting.BASE_DIR,type,name)
    if  os.path.exists(path):
        if os.path.exists('%s/%s/%s'%(setting.BASE_DIR,type,name)):
            with open('%s/%s/%s'%(setting.BASE_DIR,type,name),'rb') as f:
                return pickle.load(f)
