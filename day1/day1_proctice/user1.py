#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Auther Jmz


# 第一版
# user_db1.txt  用于存储锁定的用户

users = {
    'jmz':{'passwd':'123'}
    ,'aaa':{'passwd':'aaa'}
    ,'bbb':{'passwd':'bbb'}
}

tlag = True

while tlag:
    name = input('username:')
    if name not in users:
        print('登陆用户不存在')
        break

    with open('user_db1.txt','r',encoding='utf-8') as f:
        user_data = f.read().strip().split('\n')
        if name in user_data:
            print('用户已锁')
            break

    count = 0
    while tlag:
        passwd = input('passwd:')
        if users[name]['passwd'] == passwd:
            print('登陆成功')
            tlag = False
        else:
            count += 1
            if count >=3 :
                tlag = False
                print('用户锁定')
                with open('user_db1.txt','a',encoding='utf-8') as lock_f:
                    lock_f.write(name+'\n')





