#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os

BASE_DIR = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    os.pardir
))

DB_BASE = '%s/db/'%BASE_DIR

DB_HOSTS_DIR = '%s/hosts/'%DB_BASE

DB_HOSTS_FILE =  '%s/hosts.ini'%DB_HOSTS_DIR

DB_CHAR = 'utf-8'


