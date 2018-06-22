#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from lib.common import echo
from interface import hosts_interface

def add():
    name = input('主机名>>>').strip()
    ip = input('ip地址>>>').strip()
    port = input('端口>>>').strip()
    username = input('用户名>>>').strip()
    passwd = input('密码>>>').strip()
    keyfile = input('私钥文件>>>').strip()
    status,msg = hosts_interface.add(name,ip,port,username,passwd,keyfile)
    echo(msg)

def cat():
    try:
        data = hosts_interface.cat_all()
        for k in data:
            echo(k.center(50,'-'))
            for kk in data[k]:
                echo('%15s : %s'%(kk,data[k][kk]))
    except Exception:
        echo('主机信息有误')

def remove():
    name = input('您要删除的主机名>>>').strip()
    value = input('请输入需要删除的字段不填写则删除主机下内容（如ip）>>>').strip()
    status,msg = hosts_interface.remove(name,value)
    echo(msg)

def save():
    name = input('您要修改的主机名>>>').strip()
    ip = input('ip地址>>>').strip()
    port = input('端口>>>').strip()
    username = input('用户名>>>').strip()
    passwd = input('密码>>>').strip()
    keyfile = input('私钥文件>>>').strip()
    status,msg = hosts_interface.save(name,ip,port,username,passwd,keyfile)
    echo(msg)


hosts_view = {
    '1':add,
    '2':remove,
    '3':save,
    '4':cat
}

def run():
    while True:
        print('''
---------主机管理------
    1、添加主机
    2、删除主机
    3、修改主机
    4、查看主机        
    q、退出
        ''')
        chooise = input('>>>').strip()
        if chooise == 'q': break
        if chooise in hosts_view:
            hosts_view[chooise]()
            continue
        echo('内容有误')


if __name__ == '__main__':
    run()