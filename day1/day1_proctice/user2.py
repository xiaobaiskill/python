#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Auther Jmz


#  第二版
# 无论程序执行多少次，用户只要连续输入三次错误，用户就会被锁住。
import json

# 先将数据存在文件中
# data = {'jmz':{'passwd':'123','count':0},'aaa':{'passwd':'aaa','count':0},'bbb':{'passwd':'bbb','count':0}}
# with open('user_db2.txt', 'w', encoding='utf-8') as w_user_f:
#  json.dump(data, w_user_f)


# 读取用户数据
with open('user_db2.txt','r',encoding='utf-8') as user_f:
    users= json.load(user_f)


name = input('name:')
if name not in users:
    print('用户不存在')
elif users[name]['count'] >= 3:
    print('用户已锁')
else:
    while True:
        pwd = input('passwd:')
        if pwd == users[name]['passwd']:
            print('登录成功')
            users[name]['count'] =0
            with open('user_db2.txt', 'w', encoding='utf-8') as w_user_f:
                json.dump(users, w_user_f)
            break
        else :
            users[name]['count'] += 1
            with open('user_db2.txt', 'w', encoding='utf-8') as w_user_f:
                json.dump(users,w_user_f)
            if users[name]['count'] >=3:
                print('用户已锁')
                break

