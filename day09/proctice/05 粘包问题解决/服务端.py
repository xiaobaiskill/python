#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from socket import *
import subprocess,struct,json


server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

server.bind(('127.0.0.1',8082))

server.listen(5)

conn,client_addr=server.accept()

while True:
    try:
        cmd = conn.recv(1024)
        if not cmd:break

        obj = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        stdout = obj.stdout.read()
        stderr = obj.stderr.read()

        header_msg = {'cmd':cmd.decode('utf-8'),'total_size':len(stdout)+len(stderr)}



        header_json = json.dumps(header_msg)
        header_total = struct.pack('i',len(header_json))     # 将数字转成16进制数的 4bytes  的bytes类型值

        conn.send(header_total)                     # 发送报头 4 bytes 的 数据
        conn.send(header_json.encode('utf-8'))      # 发送 报头数据
        conn.send(stdout+stderr)                    # 发送内容数据
    except Exception as e:
        break

conn.close()

server.close()








