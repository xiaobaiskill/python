#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Auther Jmz


#  磁盘读取操作

# with open('file.txt','r',encoding='utf-8') as f :
#     for line in f.readlines():
#         print( line.split(':')[2].strip() == '0')


# 磁盘写操作

# with open('file.txt','w',encoding='utf-8') as f:
#     f.write('das:dsa:0\njmz:123:1\n')

with open('file.txt','r',encoding='utf-8') as f :
    data = f.read().strip().split('\n')
    print(data)
    if 'jmz' in data:
        print('ok')

