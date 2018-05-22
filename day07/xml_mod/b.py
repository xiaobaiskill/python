#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



import xml.etree.ElementTree as ET

tree = ET.parse('b.xml')
root = tree.getroot()           # 获取内容主体
# print(root)
#
# print(tree.find('country'))         # 返回第一个country子节点元素
# print(tree.findall('country'))      # 返回所有的country子节点元素
# print(tree.iter('year'))            # 返回所有的 year 元素


# 遍历
for country in tree.findall('country'):
    rank = country.find('rank')
    print('%s-->%s-->%s'%(rank.tag,rank.attrib,rank.text))

# tag 标签
# attrib 获取的是元素的属性
# text 获取元素的文本内容
# {'updated': 'yes'}---->2
# {'updated': 'yes'}---->5
# {'updated': 'yes'}---->69





# 增加元素
country2 = ET.Element('country')    # 创建一个新元素
country2.text='jmz'
country2.attrib = {'updated':'yes','version':'1.0'}
root.append(country2)     # 主体部分 添加一个新元素

tree.write('new.xml',encoding='utf-8')    # tree



# 修改
for year in tree.iter('year'):
    year.text = str(2016)    # xml 必须是str类型
    year.set('updated','yes')
    year.set('version','1.0')

tree.write('b.bat.xml')




