#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import socket

# 拿起电话
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 拨打电话
phone.connect(('127.0.0.1',8080))


# 说话
phone.send('hi 中国'.encode('utf-8'))

# 接受数据
data= phone.recv(1024)
print(data)

# 关闭
phone.close()

