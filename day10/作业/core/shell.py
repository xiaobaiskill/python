#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import re
from lib.common import echo

class shell:
    def __init__(self):
        pass
    def cmd(self):
        pass
    def put(self):
        pass


def run():
    while True:
        cmd = input('>>>').strip()
        res = re.search('(?:batch_run|batch_scp)\s+?-h(.*)?-g(.*)?(?:-cmd|-action)(.*)',cmd)
        if not res:echo('格式有误')
        if cmd.startswith('batch_run'):
            pass
        else:
            pass





