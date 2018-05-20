
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import xml.etree.ElementTree as ET


tree = ET.parse('a.xml')

root = tree.getroot()


# print(root.findall('country'))    # 返回所有的 country的生成器

# print(root.find('country'))


print(root.tag)
print(root.attrib)
