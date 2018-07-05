#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib.common import echo

def member_run():
    from core import member
    member_info = {
        '1':member.register
        ,'2':member.login
        ,'3':member.buy_vip
        ,'4':member.cat_video
        ,'5':member.download_video
        ,'6':member.cat_video_log
        ,'7':member.cat_notice
    }
    while True:
        print('''
------- 欢迎进入用户页面 -----
    1、注册
    2、登录
    3、冲会员
    4、查看视频
    5、下载视频
    6、查看观影记录（没有观影）
    7、查看公告
    q、退出
        ''')
        chooise = input('>>>').strip()
        if chooise == 'q':break
        if chooise in member_info:
            member_info[chooise]()
        else:
            echo('输入有误')


def manger_run():
    from core import manager
    manager_info = {
        '1':manager.register
        ,'2':manager.login
        ,'3':manager.upload_video
        ,'4':manager.rm_video
        ,'5':manager.notice_push
        ,'6':manager.member_lock
        ,'7':manager.member_unlock
    }
    while True:
        print('''
------- 欢迎进入管理界面 -----
    1、注册
    2、登录
    3、上传视频
    4、删除视频
    5、公布公告
    6、锁定用户
    7、解锁用户
    q、退出
        ''')
        chooise = input('>>>').strip()
        if chooise =='q':break
        if chooise in manager_info:
            manager_info[chooise]()
        else:
            echo('输入有误')


