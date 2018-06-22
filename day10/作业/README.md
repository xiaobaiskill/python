# 主机批量管理系统
## 菜单页面

* 1 主机管理  --> 对主机的管理操作
* 2 命令窗口  --> 通过命令行对主机进行统一命令处理

## 命令运行

* 运行start.py 文件即可
```
再此之前你可先执行 db/db_handle.py， 添加主机。（主机管理操作亦可）
```

* 命令行窗口执行命令如下
    * 1、batch_run  -h h1,h2,h3   -g web_clusters,db_servers  -cmd  "df -h"　
    * 2、batch_scp   -h h1,h2,h3   -g web_clusters,db_servers  -action put  -local test.py  -remote /tmp/test.py
```
文件的上传和下载需指定到文件
``` 


## 另外说明
```
本作业没有实现multiprocessing 并发效果
主机不能含有中文
```
