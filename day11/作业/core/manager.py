#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import os
from lib.common import echo
from interface import manager_interface
from interface import video_interface
from core import video

manager_info = {}

def auth(func):
    def wrapper(*args,**kwargs):
        global  manager_info
        if not manager_info:
            while True:
                user = input('请输入姓名：').strip()
                passwd = input('请输入密码').strip()
                status, msg = manager_interface.login(user, passwd)
                if status:
                    echo('登陆成功')
                    manager_info =msg
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
            status,msg = manager_interface.register(user,passwd)
            echo(msg)
            if status:break
        else:
            echo('两次密码不一致')

def login():
    global manager_info
    while True:
        user = input('输入姓名：').strip()
        passwd = input('输入密码').strip()
        status,msg = manager_interface.login(user,passwd)
        if status:
            echo('登陆成功')
            manager_info = msg
            break
        else:
            echo(msg)

@auth
def upload_video():
    file = input('请输入上传的视频文件路径：').strip()
    client_video = video.client_video()
    status, msg = client_video.put(r'%s'%file)
    echo(msg)
    if status:
        video_interface.video_push(os.path.basename(file))
@auth
def rm_video():
    file = input('请输入要删除的视频名>>').strip()
    status,msg = video_interface.del_video(os.path.basename(file))
    echo(msg)

@auth
def notice_push():
    from interface import notice_interface
    while True:
        title = input('请输入公告标题：').strip()
        content = input('请输入公告内容').strip()
        status,msg = notice_interface.notice_push(title,content)
        echo(msg)
        if status:break

@auth
def member_lock():
    from interface import member_interface
    data = member_interface.find()
    if data:
        print('----- %s -----'%'用户列表')
        name_info = []
        count = 0
        for info in data:
            if info['lock'] == 0:
                count += 1
                name = info['user']
                print('%s %s'%(count,name))
                name_info.append(name)
        if name_info:
            while True:
                user = input('请输入锁定的用户名：').strip()
                if user in name_info:
                    status,msg = member_interface.member_lock(user,1)
                    echo(msg)
                    if status:
                        return None
                else:
                    echo('该用户非可锁定用户')

        echo('暂无可锁用户')


@auth
def member_unlock():
    from interface import member_interface
    data = member_interface.find()
    if data:
        print('----- %s -----'%'用户列表')
        name_info = []
        count = 0
        for info in data:
            if info['lock'] == 1:
                count +=1
                name = info['user']
                print('%s %s'%(count,name))
                name_info.append(name)
        if name_info:
            while True:
                user = input('请输入解锁的用户名：').strip()
                if user in name_info:
                    status,msg = member_interface.member_lock(user,0)
                    echo(msg)
                    if status:
                        return None
                else:
                    echo('该用户非锁定用户')

        echo('暂无可解锁用户')
