#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz

import re


# str = 'hello world ,this is china!!!, welcome to beijing!'
# result = re.match('(\w*)\s(\w*)\s.*?(\w*)\s(.*)',str)
# print(result)
# print(result.group())
# print(result.span())


sql = input('sql>>')
result = re.match('.*?delete\s+?from\s+?(\w+)(\s+?where(.*))?',sql)
if result:
    print(result.groups())
else:
    print('SQL语句有问题：delete')
