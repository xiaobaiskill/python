#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import socket
server = socket.socket(socket.AF_INET,type = socket.SOCK_STREAM)   # 创建服务器套接字
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8086))
server.listen(5)
conn,client_addr = server.accept()
data1 = conn.recv(5)
print(data1.decode('utf-8'))
data2 = conn.recv(5)
print(data2.decode('utf-8'))
conn.close()
server.close()