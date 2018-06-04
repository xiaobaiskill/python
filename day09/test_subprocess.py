#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



import subprocess

res = subprocess.Popen(
    'ls',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)


print(res.stdout.read().decode('utf-8'))