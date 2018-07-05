#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os
from db import db_handle

def find():
    data = db_handle.select('video')
    return data


def video_push(file):
    info ={}
    info['file'] = file
    info['del'] = 0
    db_handle.save('video',os.path.basename(file),info)
    return True,'保存成功'

def del_video(file):
    return True,'删除成功'