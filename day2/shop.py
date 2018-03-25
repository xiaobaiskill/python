#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther Jmz
shop = [
    ['aaa',12000]
    ,['bbb',30]
    ,['ccc',4500]
    ,['ddd',129]
    ,['eee',450]
]
seleted =[]
money = int(input("your money:"))
while True:
    j = 0
    for i in shop :
        j +=1
        if i[1] < money :
            print(j,':',i[0],'>>',i[1])
    select = input('your select:')
    if select == 'q':
        print(seleted)
        break
    else :
        seleted.append(shop[int(select)-1])