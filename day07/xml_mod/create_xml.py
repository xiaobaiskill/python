#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import xml.etree.ElementTree as ET

new_xml = ET.Element('namelist')
name = ET.SubElement(new_xml,'jmz',attrib={'updated':'yes'})   # 创建子节点
age = ET.SubElement(name,'age',attrib={'year':'1994'})
age.text = 'jmz'
sex = ET.SubElement(name,'sex',text='男')
sex.text = '男'

name2 = ET.SubElement(new_xml,'jly',attrib={'updated':'yes'})
age2 = ET.SubElement(name2,'age',attrib={'year':'1994'})
age2.text = 'jly'
sex2 = ET.SubElement(name2,'sex')
sex2.text = '女'

object = ET.Element('object')
object.text = 'oldboy'
object.attrib={'addr':'shanghai','time':'2018-01-01'}


et=ET.ElementTree(new_xml)
et.write('namelist.xml',encoding='utf-8',xml_declaration=True)

ET.dump(new_xml)