#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import configparser

conf  = configparser.ConfigParser()
conf.read('example.ini',encoding='utf-8')
conf.set('bitbucket.org','User','hg')
conf.set('topsecret.server.com','Host Port','22')
conf.write(open('example.ini','w'))


