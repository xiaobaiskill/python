#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import re,paramiko,os
from lib.common import echo
from conf.settings import DB_CHAR
from interface import hosts_interface
from multiprocessing import Process

class shell():
    def __init__(self,*args):
        self.transport = {}
        self.hosts_info = {}
        for name in args:
            try:
                name=name.strip()
                hosts = hosts_interface.cat_name_info(name)
                self.hosts_info[name] = hosts
                transport = paramiko.Transport((hosts['ip'],int(hosts['port'])))
                if hosts['private_key']:
                    private_key = paramiko.RSAKey.from_private_key_file(hosts['private_key'])
                    transport.connect(username = hosts['username'],pkey=private_key)
                else:
                    transport.connect(username=hosts['username'],password=hosts['passwd'])
                self.transport[name]=transport
            except Exception:
                echo('%s 主机连接有误'%name)

    def exec(self,cmd):
        cmd = cmd.strip(r'" ')
        for name in self.transport:
            try:
                ssh = paramiko.SSHClient()
                ssh._transport = self.transport[name]
                stdin,stdout,stderr = ssh.exec_command(cmd)
                echo('-------- %s:%s --------'%(name,self.hosts_info[name]['ip']))
                echo('%s%s'%(stdout.read().decode(DB_CHAR),stderr.read().decode(DB_CHAR)))
            except Exception:
                echo('%s 执行命令有误'%name)

    def file_handle(self,cmd):
        cmd = cmd.strip()
        res = re.search('.*?-local(.*)?-remote(.*)', cmd)
        if res:
            local_path = res.group(1).strip()
            remote_path = res.group(2).strip()
            if cmd.startswith('put'):
                self.put_file(local_path,remote_path)
            else:
                self.get_file(local_path,remote_path)
        else:
            echo('命令格式有误')

    def put_file(self,local_path,remote_path):
        for name in self.transport:
            try:
                sftp = paramiko.SFTPClient.from_transport(self.transport[name])
                sftp.put(local_path,remote_path)
            except:
                echo('%s 数据处理出错，请确认主机是否正常'%name)

    def get_file(self,local_path,remote_path):
        for name in self.transport:
            try:
                sftp = paramiko.SFTPClient.from_transport(self.transport[name])
                sftp.get(remote_path,local_path)
            except:
                echo('%s 数据处理出错，请确认主机是否正常'%name)



def run():
    while True:
        cmd = input('>>>').strip()
        if cmd == 'q':break
        res = re.search('(?:batch_run|batch_scp)\s+?-h(.*)?-g(.*)?(?:-cmd|-action)(.*)', cmd)
        if not res:
            echo('命令有误')
            continue

        ssh = shell(*res.group(1).split(','))
        if cmd.startswith('batch_run'):
            ssh.exec(res.group(3))
        else:
            ssh.file_handle(res.group(3))

if __name__ == '__main__':
    run()



