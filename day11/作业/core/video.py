#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from socket import *
from lib.common import process,echo
import os,json,struct
class client_video(object):
    coding = 'utf-8'
    def __init__(self):
        self.request = socket(AF_INET,SOCK_STREAM)
        self.request.connect_ex(('127.0.0.1',8787))
    def header_send(self,data):
        '''
        发送数据头
        :param data:
        :return:
        '''
        header_json_data = json.dumps(data).encode(self.coding)
        header_size = struct.pack("i", len(header_json_data))
        self.request.send(header_size)
        self.request.send(header_json_data)

    def parse_header(self):
        cmd_struct_len = self.request.recv(4)
        if not cmd_struct_len: self.request.close()
        header_size = struct.unpack('i', cmd_struct_len)[0]
        header_json_data = b''
        while 0 < header_size:
            recv_data = self.request.recv(header_size)
            header_json_data += recv_data
            header_size -= len(recv_data)
        header_data = json.loads(header_json_data.decode(self.coding))
        return header_data

    def get(self,file,src_dir):
        '''
        客户端 获取文件
        file:文件
        src_dir: 保存目标路径
        :return:
        '''
        if not os.path.exists(src_dir):
            os.mkdir(src_dir)
        cmd_data = {'cmd':'get','file':file}
        self.header_send(cmd_data)
        header_data = self.parse_header()

        if not header_data['status']:
            return False,header_data['msg']
        with open(os.path.join(src_dir,file),'wb') as f:
            total_size = header_data['file_size']
            recv_size = 0
            while recv_size < total_size:
                recv_data = self.request.recv(2014)
                f.write(recv_data)
                recv_size += len(recv_data)
                process(recv_size/total_size,50,'下载进度')
        print()
        return True,'下载成功'
    def put(self,file):
        '''
        客户端上传文件
        file:下载文件
        :return:
        '''
        if not os.path.exists(file):
            return False,'文件路径不存在'
        total_size = os.path.getsize(file)
        data = {'cmd':'put','file':file,'file_size':total_size}
        self.header_send(data)
        recv_size = 0
        with open(file,'rb') as f:
            for line in f:
                self.request.send(line)
                recv_size += len(line)
                process(recv_size / total_size, 50, '上传进度')
        print()
        return True,'上传成功'
    def __del__(self):
        self.request.close()

# if __name__ == '__main__':
    # put(r'C:\Users\HASEE\Desktop\学习\egon\aaa.txt')
    # get('作业1.mp4',r'C:\Users\HASEE\Desktop\学习\egon\aaa.txt')

    # client = client_video()
    # client.put(r'C:\Users\HASEE\Desktop\学习\egon\day05\上节课复习')
    # client.get('作业.mp4',r'C:\Users\HASEE\Desktop\学习\egon')



