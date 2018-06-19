#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from socket import *

client = socket(AF_INET,SOCK_DGRAM)



while True:
    msg = input('>>:').strip()

    client.sendto(msg.encode('utf-8'),('127.0.0.1',8084))

    msg,server = client.recvfrom(1024)
    print(msg.decode('utf-8'))


