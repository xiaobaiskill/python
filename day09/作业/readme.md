## 程序结构:
```
traring/
├──README.md
├── conf    #配置文件
│   └── setting.py      #配置文件
├── lib  #组件
│   └── common.py         #函数处理文件
├── core    #主要程序逻辑都 在这个目录 里
│   ├── src.py          #统一视图
│   ├── admin.py  	    #管理者视图
│   └── user.py         #普通用户视图
├── db      #用户数据存储的地方
│   ├── db_handle.py    #db 数据处理页面
│   ├── admin       #管理用户文件夹
│   └── user        #普遍用户文件
├── ftp      #ftp 文件操作
│   ├── server.py    #ftp socket启动页
│   └── sclient        #ftp 用户页
├── ftp_user      #ftp 用户家目录层
│   └── jmz        #jmz家目录
└── start.py #入口文件

```

## 操作：
  * python start.py
  * 管理者账号 root:root

## 客户端用户操作
    * cd 路径                                               #切换目录
    * pwd                                                  #显示当前ftp项目路径
    * put 上传文件绝对路径                                   #上传文件
    * get ftp当前目录相对文件 路径保存地址（绝对路径文件夹）     #下载文件
