#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from core import common_func
from core import atm
from core import shopping


chosise_address = [
    ['银行',atm.run],
    ['购物商场',shopping.run]
]

while True:
    k = 0
    for v in chosise_address:
        print(k,v[0])
        k += 1

    chooise = input('请输入你要去的地方：').strip()
    if chooise.isdigit() and int(chooise) < k :
        chosise_address[int(chooise)][1]()
    else:
        common_func.echo('请输入指定的数字')

