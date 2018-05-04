#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from core import common_func
from core.atm_mod import accounts

product_list = [
    ['Iphone7 Plus',6500],
    ['Iphone8 ',8200],
    ['MacBook Pro',12000],
    ['Python Book',99],
    ['Coffee',33],
    ['Bike',666],
    ['pen',2]
  ]

select_good_list= {}
def shopping():
    while True:
        k = 0
        for v in product_list:
            print(k,v[0],v[1])
            k+=1
        chooise = input('请输入数字(q 退出)：').strip()
        if chooise =='q':
            return False
        elif chooise.isdigit() and int(chooise) < k:
            select_good_list[product_list[int(chooise)][0]] =select_good_list[product_list[int(chooise)][0]] +1 \
            if  product_list[int(chooise)][0] in select_good_list.keys() else 1
        else:
            common_func.echo('请输入指定的数字')

def cat_good():
    if select_good_list:
        total = 0
        for k in select_good_list:
            for v in product_list:
                if v[0] == k:
                    price = v[1]
                    total += select_good_list[k] * v[1]
                    break
            common_func.echo('%10s  %d  %f'%(k,select_good_list[k],float(price)))
        common_func.echo('\n%10s : %f'%('good total',float(total)))
        return total
    else:
        common_func.echo('暂未选择商品')
        return False

def buy_good():
    good_total = cat_good()
    if good_total:
        res = accounts.pay(float(good_total))
        if res:
            select_good_list.clear()
            common_func.echo('购买成功')