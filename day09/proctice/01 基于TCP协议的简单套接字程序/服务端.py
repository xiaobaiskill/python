#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import socket
server = socket.socket(socket.AF_INET,type = socket.SOCK_STREAM)   # 创建服务器套接字
# AF_INET  基于网络类型的套接字家族
# AF_UNIX 基于文件类型的套接字家族
# type=SOCK_STREAM 流式协议指的就是tcp协议

server.bind(('127.0.0.1',8086))
# 绑定ip和端口  请看是元组类型

server.listen(5)
# 允许 等待的最大请求数

conn,client_addr = server.accept()
# 获取请求的连接对象，和客户端的ip数据

data = conn.recv(1024)   # 一次接受最大1024 bytes
# 接受客户端发送的数据
send_data = '我再发送给你：'+data.decode('utf-8')
print(send_data)
conn.send(send_data.encode('utf-8'))

conn.close()

server.close()








