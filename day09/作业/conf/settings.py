#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import os
BASE_DIR = os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir,os.pardir))

DB_DIR = os.path.join(BASE_DIR,'db')

FTP_DIR = os.path.join(BASE_DIR,'ftp_user')

if __name__ == '__main__':
    print(DB_DIR)



