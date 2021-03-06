#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
from conf import settings
import socketserver,os,struct,json
from lib import common

class MyFtpServer(socketserver.BaseRequestHandler):
    coding = 'utf-8'
    def handle(self):

        # 初次接收 用户数据
        data_init = self.request.recv(1024)
        data_base = data_init.decode(self.coding)
        data_base = json.loads(data_base)
        self.user = data_base['user']
        self.home_dir = os.path.normpath(data_base['home_dir'])  # 用户家目录
        self.current_page = self.home_dir           # 当前访问页面
        self.data_size = data_base['data_size']

        while True:
            try:
                header_data = self.parse_header()
                if hasattr(self,header_data['cmd']):
                    func = getattr(self,header_data['cmd'])
                    func(header_data)
                else:
                    continue
            except Exception as e:
                print(e)
                self.request.close()
                break

    def header_send(self,header_data):
        '''
        统一 header 数据发送
        :param self:
        :param header_data:
        :return:
        '''
        header_data_json = json.dumps(header_data)
        header_size = struct.pack('i',len(header_data_json))
        self.request.send(header_size)
        self.request.send(header_data_json.encode(self.coding))


    def parse_header(self):
        '''
        获取解析header
        :return:
        '''
        header_size = self.request.recv(4)
        header_len = struct.unpack('i',header_size)[0]
        start_size = 0
        header_data_json = b''
        dec_size = header_len
        while start_size < header_len:
            header_data_json += self.request.recv(dec_size)
            start_size = len(header_data_json)
            dec_size = header_len - start_size

        header_data = json.loads(header_data_json.decode(self.coding))
        return header_data

    def cd(self,header_data):
        '''
        切换目录
        :return:
        '''
        if header_data['path'].startswith('/'):
            new_path = os.path.normpath(os.path.join(self.home_dir,header_data['path'].lstrip('/')))
        else:
            new_path = os.path.normpath(os.path.join(self.current_page, header_data['path']))


        if os.path.exists(new_path) and os.path.isdir(new_path):
            if new_path.startswith(self.home_dir) :
                self.current_page = new_path
                self.header_send({'status':True})
                return None

            if self.home_dir.startswith(new_path):
                self.current_page = self.home_dir
                self.header_send({'status':True})
                return None
            
        error = 'bash cd %s: No such file or directory'%header_data['path']
        self.header_send({'status':False,'data_size':len(error)})
        self.request.send(error.encode(self.coding))

    def pwd(self,header_data):
        self.request.send(self.current_page.encode(self.coding))

    def ls(self,header_data):
        file_and_dir = os.listdir(self.current_page)
        if file_and_dir:
            file_and_dir_json = json.dumps(file_and_dir)
            header_data = {'status':True,'data_size':len(file_and_dir_json)}
            self.header_send(header_data)
            self.request.send(file_and_dir_json.encode(self.coding))
        else:
            header_data={'status':False}
            self.header_send(header_data)

        pass
    def put(self, header_data):
        '''
        服务端接受客户端文件
        :return:
        '''

        total_size = common.getdirsize(self.home_dir) + int(header_data['file_size'])
        if total_size > int(self.data_size):
            self.header_send({'status':False,'msg':'空间不足，无法上传'})
        else:
            self.header_send({'status': True})
            start_size = 0
            with open(os.path.join(self.current_page,os.path.basename(header_data['file'])),'wb') as f:
                while start_size < header_data['file_size']:
                    data = self.request.recv(1024)
                    f.write(data)
                    start_size+=len(data)

    def get(self,header_data):
        '''
        客户端下载 服务端文件
        :return:
        '''
        current_file = os.path.join(self.current_page,header_data['file'])
        if os.path.isfile(current_file):
            self.header_send({'status': True,'file_size':os.path.getsize(current_file)})
            with open(current_file,'rb') as f:
                for line in f:
                    self.request.send(line)
        else:
            self.header_send({'status':False,'msg':'文件不存在'})




if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8081),MyFtpServer)
    server.serve_forever()
