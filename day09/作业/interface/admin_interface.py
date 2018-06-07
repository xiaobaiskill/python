#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from lib.common import encry


def login(user,pwd):
    user_data = db_handle.select(user,'admin')
    if user_data and user_data['pwd'] == encry(pwd):
        return True,user_data
    else:
        return False,'用户名或密码有误'



