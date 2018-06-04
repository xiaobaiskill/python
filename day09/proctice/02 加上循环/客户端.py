#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect_ex(('127.0.0.1',8086))
#  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常


while True:
    msg = input('我的发送：').strip()
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()


