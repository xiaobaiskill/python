#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther Jmz

info = {
    'stu001':'xiaobaiskill',
    'stu002':'aqqc',
    'stu003':'wh',
}
print('查'.center(50,'-'))
print(info['stu001'])         # 获取
print(info.get('stu006'))      # 同上，但若key不存在则只返回None  不存报错

print('改'.center(50,'-'))
info['stu001'] = '菜鸟小白'    # 存在修改，不存在添加
print(info)

print('增'.center(50,'-'))
info['stu004'] = 'lalal'
print(info)

print('删'.center(50,'-'))
del info['stu003']               #python 中的统一删
print(info.pop('stu001'))       # 删除并推出
info.popitem()              # 随机删
print(info)

print('判断数据是否存在'.center(50,'-'))
print('stu005' in info)        # 标准用法 确认stu005 是否在 info中，在返回true 不存在返回false