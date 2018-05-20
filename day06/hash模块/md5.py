#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import hashlib

m1= hashlib.md5()                   # 创建 一个md5的工厂
m1.update('中文'.encode('utf-8'))    # 向 工厂中添加内容   # 注意内容必须是 bytes类型
print(m1.hexdigest())               # 得到hash 结果，md5 是固定32位的 hash算法加密




m2 = hashlib.sha512()
m2.update(b'hello')
m2.update(b'jmz')
m2.update(b'shanghai')
m2.update(b'haha')
print(m2.hexdigest())     # sha512 是可变长的 hash算法加密
