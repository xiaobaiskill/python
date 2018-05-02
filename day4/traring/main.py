#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from config import config
from core import common

while True:
    k = 0
    for v in config.CHOOISE_ADDRESS:
        print(k,v[0])
        k +=1

    chooise = input('请输入你要去的地方：').strip()
    if chooise.isdigit() and int(chooise) < k :
        config.CHOOISE_ADDRESS[int(chooise)][1]()
    else:
        common.echo('请输入指定的数字')

