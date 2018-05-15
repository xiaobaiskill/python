#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import re


num1 = '-1 + 2 * 9 / ((3 * 2) + 1) - 1 + ((3 - 6) + 7)*3 -4'
res = re.sub('\s*','',num1)







def comput(res):

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




