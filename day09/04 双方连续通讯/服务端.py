#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import socket

# 1准备电话
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#2 查卡
phone.bind(('127.0.0.1',8080))


# 监听电话
phone.listen(5)# 半连接池   # 等待请求数


# 获取来电人的电话
conn,client_addr = phone.accept()


while True:
    try:
        # 接受电话信息
        data = conn.recv(1024)            # 客户端发送空值，  还像没接受
        if not data:
            break       # mac 客户端 单方面断开  只会返回空
        print(data)
        # 发送数据
        msg = input('>>>').strip()
        conn.send(msg.encode('utf-8'))
    except Exception as a:          # windows 单方面断开会报错
        break


conn.close()

phone.close()
