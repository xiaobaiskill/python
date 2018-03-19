#!/usr/bin/env python
# Auther Jmz
'''请使用python passwd.py 执行'''
import getpass
username = 'jmz'
password = '123123'

count = 0
while count < 3:
    user = input('username:')
    pwd =getpass.getpass('password:')
    if username == user and pwd == password :
        print('login success')
        break
    else :
        print('please input...')
    count +=1
else:
    print('username suoding')