#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import logging
logging.basicConfig(
    filename='access.log',
    format = '%(asctime)s - %(name)s -%(levelname)s -%(module)s:%(message)s',
    datefmt='%Y-%m-%d %X',
    level=10,       # 可以接受的至少什么等级的错误
)



logging.debug('这是一个调试错误')
logging.info('这是一个info错误')
logging.warning('这是一个warining错误')
logging.error('这是一个error错误')
logging.critical('这是一个critical错误')











