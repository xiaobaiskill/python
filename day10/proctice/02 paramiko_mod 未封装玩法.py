#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import paramiko
# 创建ssh对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
# 无 秘钥登陆方式
#ssh.connect(hostname='192.168.33.110',port=22, username='vagant',password='vagrant')

# 有秘钥登陆方式
private_key = paramiko.RSAKey.from_private_key_file(r'D:\vagrant2\.vagrant\machines\default\virtualbox\private_key')
ssh.connect(hostname='192.168.33.110',port=22, username='vagrant',pkey=private_key)

# 执行命令
stdin,stdout,stderr = ssh.exec_command('df')

# 获取命令结果
result =stdout.read()
print(result.decode('utf-8'))

#关闭连接
ssh.close()

