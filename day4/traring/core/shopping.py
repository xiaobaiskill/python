#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

from conf import config
from core.shopping_mod import shopping
from core import common_func

shopping_chooise = [
    ['购物',shopping.shopping]
    ,['查看所选商品',shopping.cat_good]
    ,['购买所选商品',shopping.buy_good]
]
def run():
    config.LOGIN_USER['user'] = None
    while True:
        k =0
        for v in shopping_chooise:
            print(k,v[0])
            k+=1
        chooise = input('您的选择是（q退出）：').strip()
        if chooise == 'q':
            return False
        elif chooise.isdigit() and int(chooise) < k:
            shopping_chooise[int(chooise)][1]()
        else:
            common_func.echo('请输入正确的指令')





