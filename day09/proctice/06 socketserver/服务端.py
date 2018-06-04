#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import subprocess,struct,json
import socketserver

# 通讯循环类

class MyTcpHandle(socketserver.BaseRequestHandler):
    def handle(self):
        conn=self.request
        while True:
            try:
                cmd = conn.recv(1024)
                if not cmd:break

                obj = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

                stdout = obj.stdout.read()
                stderr = obj.stderr.read()

                header_msg = {'cmd':cmd.decode('utf-8'),'total_size':len(stdout)+len(stderr)}

                header_json = json.dumps(header_msg)
                header_total = struct.pack('i',len(header_json))     # 将数字转成16进制数的 4bytes  的bytes类型值

                conn.send(header_total)                     # 发送报头 4 bytes 的 数据
                conn.send(header_json.encode('utf-8'))      # 发送 报头数据
                conn.send(stdout+stderr)                    # 发送内容数据
            except Exception as e:
                break

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8083),MyTcpHandle)
    server.serve_forever()

