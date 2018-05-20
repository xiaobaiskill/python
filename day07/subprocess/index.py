#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import subprocess


# 开启子进程执行
res = subprocess.Popen('ls -l'
                       ,shell=True
                       ,stdout=subprocess.PIPE
                       ,stderr=subprocess.PIPE)


print(res.stdout.read().decode('Utf-8'))



