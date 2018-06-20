#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import configparser

conf = configparser.ConfigParser()
conf.read('example.ini',encoding='utf-8')

res = conf.add_section('jjj.com')
conf.set('jjj.com','port','22')
conf.set('jjj.com','usernaem','jjj')

conf.write(open('example.ini','w'))

