#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import socket

xshell = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

xshell.connect(('127.0.0.1',8083))

while True:
    cmd = input('>>>').strip()
    if not cmd:
        continue
    xshell.send(cmd.encode('utf-8'))
    data = xshell.recv(1024)
    if  data.decode('utf-8') == 'none':
        continue

    print(data.decode('utf-8'),end="")

xshell.close()


