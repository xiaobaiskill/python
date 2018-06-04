#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect_ex(('127.0.0.1',8086))
client.send(b'h')
client.send(b'e')
client.send(b'll')
client.send(b'o')
client.send(b'world')
client.close()


