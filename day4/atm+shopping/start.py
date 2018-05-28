#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import os,sys
from core import src

sys.path.append(os.path.dirname(__file__))


do_thing ={'1':src.atm, '2':src.shopping}

def run():
    while True:
        print('''
    -----请选择的你要取的地方
        1. atm
        2. 购物    
        q. 退出
        ''')
        chooise = input('>>>').strip()
        if chooise == 'q':
            return ''
        elif chooise in do_thing:
            do_thing[chooise]()


USER_INFO = {}




