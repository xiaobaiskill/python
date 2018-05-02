#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from config import config
from core import common

def run():
    while True:
        k =0
        for v in config.ATM_CHOOISE:
            print(k,v[0])
            k+=1
        chooise = input('请输入你的选择:').strip()
        if chooise.isdigit() and int(chooise) < k:
            pass
        elif chooise == 'q':
            break
        elif chooise:
            common.echo('请输入正确的指令')


