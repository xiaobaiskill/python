#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os
from db import db_handle

def find(name = None):
    data = db_handle.select('video',name)
    return data


def video_push(file):
    info ={}
    info['file'] = file
    info['del'] = 0
    db_handle.save('video',os.path.basename(file),info)
    return True,'保存成功'

def del_video(file):
    data = find(file)
    info = data[0]
    if not info:
        return False,'视频不存在'
    info['del'] = 1
    db_handle.save('video',os.path.basename(info['file']),info)
    return True,'删除成功'