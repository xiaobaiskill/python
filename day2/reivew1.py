#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 一、数据类型
# 数字类型
#       整型 长整型 浮点型 附属
#字符串
# 字节串 bytes
# 列表 list
# 元组
# 字典
# 集合




# 字符串
str1 = 'jmz'
print(len(str1))        #len 返回字符串长度   数字

str2 = ' \nthis is shanghai    \n '
print(str2.strip())        # strip 去除字符串两边的换行和空白
print(str2.lstrip())       # lstrip 去除字符串左边的换行符和空白符
print(str2.rstrip())       # rstrip 去除字符串右边的换行符和空白符

str3 = 'hello WORLD'
print(str3.upper())         # upper 小写转大写
print(str3.lower())         # lower 大写转小写
print(str3.swapcase())      # swapcase 大小写相互转化

str4 = 'jmz is a boy'
print(str4.startswith('jmz'))  # startswith 是否以jmz开头
print(str4.endswith('oy'))      # endswith 是否已oy结尾

str5 = 'this is digint 7 a number'
print(str5.split())            # split 将字符串分割成列表， split默认已空格分割
print(set(str5.split()))        # set 集合去重
print(str5.rsplit(' ',2))      # 从右边开始分割

str6 = 'helloworld'
print(' '.join(['hello','world','this','is','china']))  # 已空格 拼接数组内的每一个元素
print(str6.replace('world',' jmz'))                     # 替换
print(str6.isdigit())                                   # 判断是否是数字





print('了解部分'.center(50,'-'))


strs1 = 'jmz say hello'
print(strs1.find('s',1,10))  # 包头不包尾原则，找到则显示下标 找不到返回-1
print(strs1.index('s',1,8))  # 同上但 找不到会报错
print(strs1.count('l',1,4))  # 包头不包尾  记录字符出现的次数

print(strs1.center(40,'-'))  # 内容显示在中间
print(strs1.ljust(40,'-'))  # 内容显示在左边
print(strs1.rjust(40,'-'))  # 内容显示在右边
print(strs1.zfill(50))      # 用0填充

strs2 = 'hello\tworld! this Is jmZ'
print(strs2.expandtabs(10))  # 将tab转化成10个空格
print(strs2.capitalize())      # 首字母大写 其他小写
print(strs2.title())            # 单词首字母大写 其他小写
print(strs2.swapcase())         # 大小写反转





print('is 数字系列'.center(50,'-'))
num1 = b'4' # bytes
num2 = u'4' # unicode
num3 = '四'
num4 = 'Ⅳ'
num = 4


# isdigt:unicode bytes
print(num1.isdigit())
print(num2.isdigit())
print(num3.isdigit())
print(num4.isdigit())

print()
#isdecimal:nuicode
# bytes 类型5无 isdecimal 方法
print(num2.isdecimal())
print(num3.isdecimal())
print(num4.isdecimal())

print()
# isnumberic:unicode,中文数字，罗马数字
#不能理解如何会无法使用isnumberic
print(num2.isnumeric())
print(num3.isnumeric())
print(num4.isnumeric())


print()
# 无法判断是否是浮点型
num5 = '4.5'
print(num5.isdigit())
print(num5.isdecimal())
print(num5.isnumeric())



print()
print('is 其他类型的'.center(50,'-'))
strss1 = 'jmz123  '
print(strss1.isalnum())    # 是否是由字母或数字组成
print(strss1.isalpha())    #是否是由字母组成
print(strss1.isspace())    # 是否是空格
print(strss1.isidentifier())



print()
strss2 = 'dhello world this is china'
print(strss2[:3])
print(strss2[2])
print(strss2[-2:])
print(strss2.find('e'))
print(strss2[0:-1])





