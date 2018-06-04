#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import socket
server = socket.socket(socket.AF_INET,type = socket.SOCK_STREAM)   # 创建服务器套接字
# AF_INET  基于网络类型的套接字家族
# AF_UNIX 基于文件类型的套接字家族
# type=SOCK_STREAM 流式协议指的就是tcp协议

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 加入一条socket配置，重用ip和端口,如果存在则重用 ip和端口

server.bind(('127.0.0.1',8086))
# 绑定ip和端口  请看是元组类型

server.listen(2)
# 允许 等待的最大请求数


# 获取请求的连接对象，和客户端的ip数据

while True:
    conn, client_addr = server.accept()
    while True:
        try:
            data = conn.recv(1024)   # 一次接受最大1024 bytes
            if not data: break       # 用于 linux ，当用户端口连接时，发送一个b''
            # 接受客户端发送的数据
            print(data.decode('utf-8'))
            msg = input('我的回复：').strip()
            conn.send(msg.encode('utf-8'))
        except Exception as e:
            break   # 用于windows ,当客户端断开时，报错
    conn.close()

server.close()








