#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import socket,subprocess.os

xshell = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
xshell.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)


xshell.bind(('127.0.0.1',8083))


xshell.listen(5)

conn,client_addr = xshell.accept()

while True:
    try:
        cmd = conn.recv(1024)
        if not cmd:break

        res = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout = res.stdout.read()
        stderr = res.stderr.read()

        if not stdout and not stderr:
            conn.send('none'.encode('utf-8'))
            continue

        conn.send(stdout)
        conn.send(stderr)
    except Exception:
        break

conn.close()

xshell.close()