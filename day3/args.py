#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 函数
# args  非固定参数，会已元组方式保存



def echo(name,age,*args):
    print(name,age,args)


echo('jmz','23','SH','PY')

echo(age=23,name='jmz')

