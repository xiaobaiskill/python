#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import socket
import json,struct,os
from lib.common import echo,process_bar

class client_ftp(object):
    ip_addr = ('127.0.0.1',8081)
    type =  socket.SOCK_STREAM
    family = socket.AF_INET
    coding = 'utf-8'
    def __init__(self,data):
        self.client = socket.socket(self.family,self.type)
        try:
            self._connect()
            self._init(data)
        except Exception as e:
            self._close()

    def _connect(self):
        '''
        连接socket
        :param self:
        :return:
        '''
        self.client.connect_ex(self.ip_addr)

    def _init(self,data):
        '''
        初始化数据
        :param self:
        :param data:
        :return:
        '''
        self.client.send(json.dumps(data).encode(self.coding))

    def _close(self):
        '''
        关闭socket
        :param self:
        :return:
        '''
        self.client.close()

    def run(self):
        '''
        运行
        :param self:
        :return:
        '''
        while True:
            try:
                cmd = input('>>>').strip()
                l = cmd.split()
                cmd = l[0]
                if hasattr(self,cmd):
                    func = getattr(self,cmd)
                    func(l)
                else:
                    echo('命令不存在')
            except Exception as e:
                print('进程关闭')
                self._close()

    def header_send(self,header_data):
        '''
        统一 header 数据发送
        :param self:
        :param header_data:
        :return:
        '''
        header_data_json = json.dumps(header_data)
        header_size = struct.pack('i',len(header_data_json))
        self.client.send(header_size)
        self.client.send(header_data_json.encode(self.coding))

    def parse_header(self):
        '''
        获取解析header
        :return:
        '''
        header_size = self.client.recv(4)
        header_len = struct.unpack('i',header_size)[0]
        start_size = 0
        header_data_json = b''
        dec_size = header_len
        while start_size < header_len:
            header_data_json += self.client.recv(dec_size)
            start_size = len(header_data_json)
            dec_size = header_len - start_size

        header_data = json.loads(header_data_json.decode(self.coding))
        return header_data


    def cd(self,cmd):
        header_data = {'cmd':cmd[0],'path':cmd[1]}
        self.header_send(header_data)
        header_data = self.parse_header()
        if not header_data['status']:
            start_size = 0
            data = b''
            while start_size < header_data['data_size']:
                data += self.client.recv(2024)
                start_size += len(data)
            print(data.decode(self.coding))

    def ls(self,cmd):
        header_data ={'cmd':cmd[0]}
        self.header_send(header_data)
        header_data = self.parse_header()
        if header_data['status']:
            data_json = self.client.recv(header_data['data_size'])
            data = json.loads(data_json)
            for info in data:
                print(info,end=' ')
            print()


    def pwd(self,cmd):
        '''
        返回服务器当前的文件路径
        :return:
        '''
        header_data = {'cmd':cmd[0]}
        self.header_send(header_data)
        data = self.client.recv(1024)
        print(data.decode(self.coding))
        pass

    def put(self,cmd):
        '''
        上传文件至服务器当前路径
        put 绝对路径文件
        :param self:
        :return:
        '''
        if os.path.isfile(cmd[1]):
            header_data = {'cmd': cmd[0], 'file': cmd[1], 'file_size':os.path.getsize(cmd[1])}
            self.header_send(header_data)
            res_data = self.parse_header()
            start_size = 0
            if res_data['status']:
                with open(header_data['file'],'rb') as f:
                    for line in f:
                        self.client.send(line)
                        start_size += len(line)
                        process_bar(start_size/header_data['file_size'])
                print()

            else:
                echo(res_data['msg'])
        else:
            echo('上传文件不存在！！！')
        pass

    def get(self,cmd):
        '''
        下载文件
        get 服务端当前文件 绝对文件夹路径地址
        :param self:
        :return:
        '''
        if not os.path.isdir(cmd[2]):
            try:
                os.mkdir(cmd[2])
            except Exception as e:
                echo('本地路径地址有误')
                return None

        header_data = {'cmd':cmd[0],'file':cmd[1]}
        self.header_send(header_data)
        res_data = self.parse_header()
        if res_data['status']:
            start_size = 0
            with open(os.path.join(cmd[2],cmd[1]),'wb') as f:
                while start_size < int(res_data['file_size']):
                    data = self.client.recv(1024)
                    f.write(data)
                    start_size += len(data)
                    process_bar(start_size / res_data['file_size'])
                print()
        else:
            echo(res_data['msg'])


if __name__ == '__main__':
    client=client_ftp({'user':'jmz','home_dir':r'D:\w_python\python\day09\作业\test','data_size':'100000'})
    client.run()