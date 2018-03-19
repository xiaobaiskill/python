#!/usr/bin/env python
# Auther Jmz
'''请使用python passwd.py 执行'''
import getpass
username = input('username:')
passwd = getpass.getpass('passwd:')
print(username,passwd)