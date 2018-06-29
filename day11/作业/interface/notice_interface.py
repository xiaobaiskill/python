#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from db import db_handle
from lib.common import hash_md5

def find():
    data = db_handle.select('notice','notice')
    return data


def notice_push(title,content):
    info ={}
    info['title'] =title
    info['content'] =content
    db_handle.save('notice','notice',info)
    return True,'发布成功'