#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import pickle

def func(name):
    print(name)

dict = {'name':'jmz','school':{'small_school':'lala','middle_school':'chajj school'},'func':func}

with open('pick.pkl','wb') as f:
    # pickle 只保存 bytes 类型的数据
    f.write(pickle.dumps(dict))    # 在转化的过程中 已自动实现
    # pickle.dump(dict,f)          # 上面方式的简写

with open('pick.pkl','rb') as f:
    res = pickle.loads(f.read())              # 读取全部和第几行无关
    # res = pickle.load(f)                   # 上面的简写

print(res)
res['func'](res['name'])




