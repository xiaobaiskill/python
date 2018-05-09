#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 字典

# ---------------定义-----------
info = {'name':'jmz','age':25}
info1 = dict(name='jmz',age=25)
info2 = dict([['name','jmz'],('age',25)])     # 列表和元组的表现显示相差不大
info3 = {}.fromkeys(('name','age','sex'),None)
print(info)
print(info1)
print(info2)
print(info3)

print()
# ----------增--------
print('增'.center(50,'-'))
info['sex'] ='nan'                       # 修改亦添加
info.setdefault('obj','SH')              # setdefault  不存在添加 存在不添加
info.setdefault('name','jjj')
print(info)




print()
# ---------- 查--------
print('查'.center(50,'-'))
print(info.get('name'))
print(info.get('name11'))             # get 获取key 值 ，不存在 None
print(info.__len__())
print(len(info))
print(info.keys())                    # 取所有的键
print(info.values())                    # 取所有的值
print(info.items())                   # 字典转列表
print(info)


print()
# ----------改--------
print('改'.center(50,'-'))
info['name'] ='kkk'                    # 增加 亦修改
b = {
    'k1':313,
    'k2':['dsada'],
    'age':55,
    'k3':{
        'g1':['das']
    }
}
info.update(b)              # 有则修改 无则添加
print(info)



print()
# ----------其他--------
print('其他'.center(50,'-'))
for i in info:
    print(i)

print('-------------')
for k,v in info.items():
    print(k,'-',v)
print(info)



print()
# ----------删--------
print('删'.center(50,'-'))
print(info.pop('name'))      # 推出并删除
print(info.popitem())           #随机删吗
print(info)