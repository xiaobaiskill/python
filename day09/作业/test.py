#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz




# def client_ftp(data_init):
#     client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     client.connect_ex(('127.0.0.1',8087))
#
#     #初始化，传输用户信息
#     client.send(json.dumps(data_init).encode('utf-8'))
#
#     # 用户操作
#     while True:
#         try:
#             cmd = input('>>>').strip()
#             if not cmd:break
#             client.send(cmd.encode('utf-8'))
#             data = client.recv(1024)
#             print(data)
#         except Exception as e:
#             print('程序终止')
#             break
#     client.close()


# s = 'cmd ss dd'
# l = s.split()
# print(l)


import os
# print(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir,os.pardir,os.pardir,os.pardir,os.pardir,os.pardir,os.pardir,os.pardir)))


# getsize 只能获取文件的数据大小
# print(os.path.getsize(__file__))  #bytes

# base_dir = os.path.normpath( os.path.join(os.path.abspath(__file__),os.pardir))

# data1 =os.path.getsize(os.path.join(base_dir,'start.py'))
# data2 =os.path.getsize(os.path.join(base_dir,'test.py'))
# data3 =os.path.getsize(os.path.join(base_dir,'需求分析'))

# # print(data,type(data))
# print(data1,type(data1))
# print(data2,type(data2))
# print(data3,type(data3))


# 通过循环获取文件大小
# def getdirsize(dir):
#    size = 0
#    for root, dirs, files in os.walk(dir):
#         size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
#         print(size)
#    return size


# 需要先创建文件夹才能创建文件
# os.mkdir('test')
# with open('test/test.txt','w',encoding='utf-8') as f:
#     f.write('dsada\n')
#     f.write('dsada\n')




#
# class test(object):
#     def dd(self):
#         print('dd')
#     def run(self):
#         func = getattr(self,'dd')
#         func()
#
# test1 = test()
# test1.run()



# dir = os.path.normpath(os.path.join('/root/test','/'.lstrip('/')))
# print(dir)


g = os.listdir('D:/w_python/python/day09/作业/test')
print(len(g))
# print(files)

# file_and_dir=next(g)
# print(file_and_dir)
# print(file_and_dir[1])
# print(file_and_dir[2],type(file_and_dir[2]))