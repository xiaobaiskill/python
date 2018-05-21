#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import random

# print(ord('A'),ord('Z'),ord('a'),ord('z'),ord('0'),ord('9'))

def make_code_one():
    '''
    随机生成以为字符
    a-z A-Z 0-9
    :return:
    '''
    s1 = random.randint(ord('a'),ord('z'))
    s2 = random.randint(ord('A'),ord('Z'))
    s3 = random.randint(ord('0'),ord('9'))
    res = random.choice([s1,s2,s3])
    return chr(res)

def make_code(n):
    res = ''
    for i in range(n):
        res = res + make_code_one()
    return res

print(make_code(4))

