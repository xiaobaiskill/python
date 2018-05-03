#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz

import re


# str = 'hello world ,this is china!!!, welcome to beijing!'
# result = re.match('(\w*)\s(\w*)\s.*?(\w*)\s(.*)',str)
# print(result)
# print(result.group())
# print(result.span())


# sql = input('sql>>')

# result = re.match('.*?delete\s+?from\s+?(\w+)(\s+?where(.*))?',sql)
#
# if result:
#     print(result.groups())
# else:
#     print('SQL语句有问题：delete')

#insert inro table('id','aaa',aa) values('id1','ass',234),('id2')
# if 'values' in sql :
#     regex = re.compile('\((.+?)\)')
#     print(regex)
#     result = regex.findall(sql.split('values')[1])
#     if result:
#         print(result)
#         print('ok')
#     else:
#         print('no')


# num = {'a':1,'b':2}
# print(num['c'] if 'c' in num.keys() else '' )

# sql = '   name="jmz" and id>2  '
# # result = re.match('\s*?(\w+)\s*?',sql)
# result = re.match('\s*?(\w+)\s*?(>|>=|<|>=|=|like)\s*?(\w+)',sql)
# if result:
#     print(result.groups())
# else:
#     print('no')
#


# sql = 'update table set name =sdad,id=2 where id =2 and name =jmz'
# result = re.match('\s*?update\s+?(\w+)\s+?set\s+?(.*?)\s*?(where(.*))?$', sql)
# print(result.groups())



# sql ='select name,age from emp '
# result = re.match('\s*?select\s+?(.*)\s+?from\s+?(.*?)\s*?(where(.*))?$',sql)
# print(result.groups())




# dict = {'name':'dsada','dsa':'dsad'}
# if dict.get('dsad'):
#     for a in dict.get('dsad'):
#         print(a)


# k='jmz'
# print('%s:表字段不存在'%k)

res = -1.33
print(res+1.38,type(res))

res1 = 1.33
print(-res1,type(-res1))