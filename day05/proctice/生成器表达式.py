#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 把 列表推导式中的[] 变成() 就是 生成器表达式
# 生成器表达式
res = (i for i in range(10000000000000000000000000000000000000000000))
print(res)
# <generator object <genexpr> at 0x00000000022AD150>



# 生成器
def test():
    yield 1

test = test()
print(test)
# <generator object test at 0x00000000021FD200>
print(next(test))
# 1









