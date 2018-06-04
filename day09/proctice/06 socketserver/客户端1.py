#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from socket import *
import json,struct

client = socket(AF_INET,SOCK_STREAM)

client.connect_ex(('127.0.0.1',8083))

while True:
    msg = input('>>>').strip()
    if not msg:
        continue
    client.send(msg.encode('utf-8'))

    header_total = client.recv(4)
    header_msg_size = struct.unpack('i',header_total)[0]
    header_msg =client.recv(int(header_msg_size))
    header_data = json.loads(header_msg)
    start_size = 0
    data = b''
    while start_size < int(header_data['total_size']):
        recv_data = client.recv(1024)
        data += recv_data
        start_size+=len(recv_data)
    print(data.decode('utf-8'))
