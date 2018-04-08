#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



end = 9

count = 1

while count <= end :
    start = 1
    while start <=count:
        print(count, '*', start, '=', start * count, end='  ')
        start += 1

    count += 1
    print()
