#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from socket import *

# 服务端对象
server = socket(AF_INET,SOCK_DGRAM)

# 绑定ip addr
server.bind(('127.0.0.1',8084))

while True:
    # 直接接受客户端IPaddr和消息
    msg,client_addr= server.recvfrom(1024)

    # 发送数据
    server.sendto(msg.upper(),client_addr)


