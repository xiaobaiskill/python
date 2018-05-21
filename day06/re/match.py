#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import re
content = 'jmz3s4[22],[3],[dsada]'

res = re.match('.*?\[(.*?)\].*?\[(.*?)\].*?\[(.*?)\]',content)

print(res.group())    # jmz3s4[22],[3],[dsada]
print(res.group(1))   # 22
print(res.group(2))   # 3
print(res.group(3))   # dsada

