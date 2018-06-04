#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect_ex(('127.0.0.1',8086))
#  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

msg = input('你要发送的东东>>>').strip()

client.send(msg.encode('utf-8'))

data = client.recv(1024)
print(data.decode('utf-8'))
# 接受最大 数据1024 bytes
client.close()


