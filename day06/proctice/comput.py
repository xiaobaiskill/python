#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import re

def comput(res):
    # 乘除法操作
    while True:
        if re.search('\d+\.?\d*[\*\/][\-]?\d+\.?\d*', res):
            result = re.search('\d+\.?\d*[\*\/][\-]?\d+\.?\d*', res).group()
            if len(result.split('*')) > 1:
                n1, n2 = result.split('*')
                value = float(n1) * float(n2)
            else:
                n1, n2 = result.split('/')
                value = float(n1) / float(n2)

            before, after = re.split('\d+\.?\d*[\*\/][\-]?\d+\.?\d*', res, 1)
            res = '%s%s%s' % (before, value, after)
        else:
            break
    # 加减法操作
    while True:
        res = re.sub('\+\+', '-', res)
        res = re.sub('\+\-', '-', res)
        res = re.sub('\-\+', '-', res)
        res = re.sub('\-\-', '+', res)

        if re.search('[\-\+]?\d+\.?\d*[\+\-]\d+\.?\d*', res):
            result = re.search('[\-\+]?\d+\.?\d*[\+\-]\d+\.?\d*', res).group()
            result = result.lstrip('+')
            if len(result.split('+')) > 1:
                n1, n2 = result.split('+')
                value = float(n1) + float(n2)
            else:
                n1, n2 = result.rsplit('-', 1)
                value = float(n1) - float(n2)

            before, after = re.split('[\-\+]?\d+\.?\d*[\+\-]\d+\.?\d*', res, 1)
            res = '%s%s%s' % (before, value, after)
        else:
            break
    return res








def exec_comput(res):
    res = re.sub('\s*', '', res)
    while True:
        if re.search('\([^\(]*?\)',res):
            result = re.search('\([^\(]*?\)',res).group()

            value = comput(result.strip('()'))
            before,after =re.split('\([^\(]*?\)',res,1)

            print('before:%s'%res)
            print(result.strip('()'),'=',value)

            res = '%s%s%s'%(before,value,after)

            print('after:%s'%res)
            print('上一次的计算结果'.center(50,'-'))

        else:
            res = comput(res)
            return res



expression='1-2*((60+2*(-3-(40.0)/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
print(exec_comput(expression))
print('eval:%s'%eval(expression))








