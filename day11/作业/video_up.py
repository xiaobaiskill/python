#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import socketserver,json,struct,os
from conf.settings import VIDEO_DIR
class MYScoket(socketserver.BaseRequestHandler):
    coding = 'utf-8'
    def handle(self):
        while True:
            try:
                header_data = self.parse_header()
                if hasattr(self,header_data['cmd']):
                    func = getattr(self,header_data['cmd'])
                    func(header_data)
                else:
                    self.header_send({'status':False,'msg':'命令有误'})
            except Exception as e:
                print('连接断开')
                break

    def header_send(self,data):
        header_json_data = json.dumps(data).encode(self.coding)
        header_size = struct.pack('i',len(header_json_data))
        self.request.send(header_size)
        self.request.send(header_json_data)

    # 报文头处理
    def parse_header(self):
        cmd_struct_len = self.request.recv(4)
        if not cmd_struct_len:self.request.close()
        struct_len = struct.unpack("i",cmd_struct_len)
        header_size = struct_len[0]
        header_json_data = b''
        while 0 < header_size:
            recv_data = self.request.recv(header_size)
            header_json_data += recv_data
            header_size  -= len(recv_data)
        header_data = json.loads(header_json_data.decode(self.coding))
        return header_data

    # 客户端获取文件
    def get(self,header_data):
        file = os.path.join(VIDEO_DIR,header_data['file'])
        if os.path.exists(file):
            header_data = {'status':True,'file_size':os.path.getsize(file)}
            self.header_send(header_data)
            with open(file,'rb') as f:
                for line in f:
                    self.request.send(line)
        else:
            self.header_send({'status':False,'msg':'文件不存在'})

    # 客户端上传文件
    def put(self,header_data):
        if not os.path.exists(VIDEO_DIR):
            os.mkdir(VIDEO_DIR)
        with open(os.path.join(VIDEO_DIR,os.path.basename(header_data['file'])),'wb') as f:
            total_size = header_data['file_size']
            recv_size = 0
            while recv_size < total_size:
                recv_data = self.request.recv(2014)
                f.write(recv_data)
                recv_size += len(recv_data)

if __name__ == '__main__':
    video_server = socketserver.ThreadingTCPServer(('127.0.0.1',8787),MYScoket)
    video_server.serve_forever()

















