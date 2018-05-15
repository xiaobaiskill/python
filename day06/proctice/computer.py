#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import re


expression='1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'


num1 = '-1 + 2 * 9 / 3 * 2 + 1 - 1 + 3 - 6 + 7*3 -4'



res = re.sub('\s*','',num1)


# 乘除法操作
while True:
    if re.search('\d+\.?\d*[\*\/]\d+\.?\d*',res):
        result = re.search('\d+\.?\d*[\*\/]\d+\.?\d*', res).group()
        if len(result.split('*')) > 1:
            n1,n2 = result.split('*')
            value = float(n1) * float(n2)
        else:
            n1,n2 = result.split('/')
            value = float(n1) / float(n2)

        before,after=re.split('\d+\.?\d*[\*\/]\d+\.?\d*', res,1)
        res = '%s%s%s'%(before,value,after)
    else:
        break

print(res)

# 加减法操作
while True:
    res = re.sub('\+\+','-',res)
    res = re.sub('\+\-','-',res)
    res = re.sub('\-\+','-',res)
    res = re.sub('\-\-','-',res)


    if re.search('[\-\+]?\d+\.?\d*[\+\-]\d+\.?\d*',res):
        result = re.search('[\-\+]?\d+\.?\d*[\+\-]\d+\.?\d*', res).group()
        result=result.strip('+')
        if len(result.split('+')) > 1:
            n1,n2 = result.split('+')
            value = float(n1) + float(n2)
        else:
            n1,n2 = result.rsplit('-',1)
            value = float(n1) - float(n2)

        before,after=re.split('[\-\+]?\d+\.?\d*[\+\-]\d+\.?\d*', res,1)
        res = '%s%s%s'%(before,value,after)
    else:
        break


print(res)





