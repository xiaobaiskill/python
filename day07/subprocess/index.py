#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import subprocess,time
# 开启子进程执行
res = subprocess.Popen('tasklist'
                       ,shell=True
                       # ,stdout=subprocess.PIPE          # 标准化输出
                       # ,stderr=subprocess.PIPE          # 错误输出
)
time.sleep(1)
print(res)
print(res.stdout.read().decode('gbk'))           # res.stdout.read() 拿到的是一个utf-8或者gbk的16进制码，这个是操作系统默认字符编码有关


# 在没有stdout=subprocess.PIPE的情况下，子进程命令结果或直接输入到终端，能否正常显示，取决于该程序的结束时间是否大于子进程的结束时间，大于则显示，小于则来不急显示
# 在有stdout=subprocess.PIPE的情况下，只有需要（res.stdout.read()）是才会显示



