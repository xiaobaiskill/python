#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import paramiko

# 创建连接对象
transprot = paramiko.Transport(('192.168.33.110', 22))

# 连接
private_key = paramiko.RSAKey.from_private_key_file(r'D:\vagrant2\.vagrant\machines\default\virtualbox\private_key')
transprot.connect(username='vagrant',pkey=private_key)

# 创建 ssh 对象
ssh = paramiko.SSHClient()
# 将transprot 放在属性中 直接使用
ssh._transport  = transprot

# 执行命令
stdin,stdout,stderr = ssh.exec_command('df')

# 获取 结果
result = stdout.read()

print(result.decode('utf-8'))

ssh.close()

