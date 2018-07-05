#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import time,os
from lib.common import echo
from core import video
from interface import member_interface
from interface import video_interface

member_info = {}
# 装饰器
def auth(func):
    def wrapper(*args,**kwargs):
        global  member_info
        if not member_info:
            while True:
                user = input('请输入姓名：').strip()
                passwd = input('请输入密码').strip()
                status, msg = member_interface.login(user, passwd)
                if status:
                    echo('登陆成功')
                    member_info = msg
                    break
                else:
                    echo(msg)
        return func(*args,**kwargs)
    return wrapper


def register():
    while True:
        user = input('输入姓名：').strip()
        passwd = input('输入密码').strip()
        confirm_passd = input('再次确认密码').strip()
        if passwd == confirm_passd:
            if not passwd:
                echo('密码不能为空')
                continue
            status,msg = member_interface.register(user,passwd)
            echo(msg)
            if status:break
        else:
            echo('两次密码不一致')


def login():
    global member_info
    while True:
        user = input('输入姓名：').strip()
        passwd = input('输入密码').strip()
        status,msg = member_interface.login(user,passwd)
        if status:
            echo('登陆成功')
            member_info = msg
            break
        else:
            echo(msg)

@auth
def buy_vip():
    global member_info
    if member_info['level'] == 0:
        while True:
            money = input('请输入充值金额>>').strip()
            if money.replace('.','',1).isdigit():
                status,msg = member_interface.buy_vip(member_info['user'],money)
                echo(msg)
                if status:
                    member_info['level']  = 1
                    break
            else:
                echo('请输入正确金额')
    else:
        echo('你已经是会员了')

@auth
def cat_video():
    for info in video_interface.find():
        echo('视频：')
        count = 0
        if info['del'] == 0:
            count +=1
            echo('     %s   %s'%(count,info['file']))
@auth
def download_video():
    if member_info['level'] != 1:
        cat_notice()
        echo('非会员用户需等待10秒广告时间')
        time.sleep(10)
    file = input('请输入视频名称》》').strip()
    info = video_interface.find(os.path.basename(file))
    if not info or info[0]['del'] == 1:
        echo('视频不存在')
        return False

    src_dir = input('保存视频至》》').strip()
    client_video = video.client_video()
    status,msg = client_video.get(file,src_dir)
    echo(msg)

@auth
def cat_video_log():
    pass

@auth
def cat_notice():
    from interface import notice_interface
    data = notice_interface.find()
    count = 0
    for info in data:
        count +=1
        print('------ 公告%s -------'%(count))
        echo('标题：%s'%info['title'])
        echo('内容：%s'%info['content'])
