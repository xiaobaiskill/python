#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import struct

total = 16374

res = struct.pack('i',total)

print(len(res))



