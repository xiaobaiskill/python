#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

list = ['jmz','jmz1','wh','qqc',['sh','py',1],1,2,3,4,5,6]
# 正向取步长
print(list[::2])
print(list[:3])    # == list[:3:1]
print(list[2:3])

# 反向取长
print(list[3::-1])

#列表反转
print(list[::-1])


#-------------------取长度-------------------
print(list.__len__())     # 取长度
print(len(list))          # 也是取长度
print(list.count('jmz'))  # 查询列表 知道数据个数   ，不填会报错

#---------------------存取--------------
print('存取'.center(50,'-'))
print(list.append('dadas'))                    #存 末尾追加
print(list.insert(2,['jjj','mmmm']))          # 存 ，从第几个下标开始插入
list.extend(['jmz11','jmz22','jmz33'])        # 列表扩展，将后面的列表扩展到list列表中
print(list.pop(1))                  # 从第几个下标取出，默认是从最后取出
print(list)

#-----------------改---------------
print('改'.center(50,'-'))
list[1] = 'jmzjmzjmzjmz'     # 改下标为1的值       这个没有添加能力
print(list)


#----------------其他-----------------
print('其他'.center(50,'-'))
list.append('jmz11')
print(list.index('jmz11',13))              # 返回首先找到的值 并返回下标       13指定开始下标
print(list)
list1 = list.copy()                         # 重写复制一份
print(list1)


#------------in    not in--------
print('in not in'.center(50,'-'))
for i in list:
    print(i)


#-----------------删-----------
print('删'.center(50,'-'))
del list[1]             # 通用删除
print(list)
list.clear()
print(list)




