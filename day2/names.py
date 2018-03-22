#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther Jmz
name = ["jmz","qqc","wh","wyc","wh","wh","wh","2dsad","#@dsa"]


print('----------增----------')
name.append('lmm')       #  最后追加
print(name)
name.insert(1,'jmh')
print(name)
name.insert(3,'xiaobai')
print(name)

print('----------改-----------')
name[0] = 'jmz2'
print(name)
print('-------------删-------')
#name.remove('qqc')
#del name[0]
#print(name.pop())                # 去除并删除
name.pop(0)
print(name)
print('--------查----------')
print(name.index('xiaobai'))
print(name[name.index("xiaobai")])
print(name.count('wh'))

print('------ 切片-------')

print(name[0])
print(name[-2:])
print(name[:3])
print(name[0:3])

print('--------排序---------')
name.sort()
print(name)

print('--------反转--------')
name.reverse()
print(name)

print('-------扩展---------')
name2 = [1 , 2 , 3 , 4]
name.extend(name2)
del name2
print(name)

print('-------------复制------')
names = name.copy()
print(names)

print('--------清空-----------')
name.clear()
print(name)
