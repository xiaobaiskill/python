#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


d={i:i for i in range(10) if i > 0}
print(d)
# {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

# 类似于：
dic = {}
for i in range(10):
    if i >0:
        dic[i] = i
print(dic)


userinfo=[('egon','123'),('alex','456'),('wxx','679')]
dic={k:v for k,v in userinfo}
print(dic)
# {'egon': '123', 'alex': '456', 'wxx': '679'}

