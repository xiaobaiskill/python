#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os,sys

BASE_DIR = os.path.normpath(
    os.path.join(os.path.abspath(__file__)
                 ,os.pardir
                 ,os.pardir)
)


DB_DIR = '%s/db'%BASE_DIR





if __name__ == '__main__':
    print(BASE_DIR)


