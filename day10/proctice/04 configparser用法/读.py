#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import configparser

res = configparser.ConfigParser()

res.read('example.ini')

print(res.sections())
print(res.options('topsecret.server.com'))
print(res.get('topsecret.server.com','host port'))

