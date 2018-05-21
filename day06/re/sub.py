#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import re

test = '+-dsad-+dsa--dd++'
print(re.sub('\+\-','-',test))
# -dsad-+dsa--dd++