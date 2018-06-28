#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os

BASE_DIR = os.path.normpath(
    os.path.join(os.path.abspath(__file__)
                 ,os.pardir
                 ,os.pardir)
)


DB_DIR = '%s/db'%BASE_DIR


ADMIN_DIR = '%s/admin'%DB_DIR

MEMBER_DIR = '%s/member'%DB_DIR

VIDEO_DIR = '%s/video'%DB_DIR

VIEW_VIDEO_LOG='%s/view_video_log'%DB_DIR



if __name__ == '__main__':
    print(BASE_DIR)


