#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import logging

# logger对象： 生成对象，产生atm日志
logger1=logging.getLogger('atm')


# handle对象, 控制日志内容的去向，文件or终端
#      FileHandler 文件
#      StreamHandler 终端
a1=logging.FileHandler('a1.log',encoding='utf-8')
a2=logging.FileHandler('a2.log',encoding='utf-8')
ch = logging.StreamHandler()

# 建立 logger 和 handle 之间的绑定关系
logger1.addHandler(a1)
logger1.addHandler(a2)
logger1.addHandler(ch)


# Formatter 对象： 定制日志格式
format1 = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s -%(module)s:%(message)s',datefmt='%Y-%m-%d %X')
format2 = logging.Formatter('%(asctime)s-%(module)s:%(message)s',datefmt='%Y-%m-%d %X')

# 为handle对象定制 日志格式
a1.setFormatter(format1)
a2.setFormatter(format2)


# 设置 保存 错误的级别     先 logger  后a1 or a2    # 先顶级过滤 logger 后 才是handle过滤
logger1.setLevel(10)
a1.setLevel(20)
a2.setLevel(30)




# 输出错误
logger1.debug('这是一个bug错误')
logger1.error('这是一个error错误')
logger1.info('这是一个info错误')
