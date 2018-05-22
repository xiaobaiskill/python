#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import configparser


# 用户对 ini 一类文件的读写操作
# 一般使用与 对环境，或系统 配置文件的 读写操作
import configparser

# 写一个example.ini 配置文件
# config = configparser.ConfigParser()    #  生成object 对象
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'time' : 12.34}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)


# 读example.ini 配置文件
res = configparser.ConfigParser()
res.read('example.ini')

print(res.sections())
print(res.options('topsecret.server.com'))

print(res.get('bitbucket.org','forwardx11'))
print(res.getint('bitbucket.org','CompressionLevel'))
print(res.getfloat('bitbucket.org','time'))
