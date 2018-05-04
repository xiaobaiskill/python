
# 程序结构:
```
traring/
├──README.md
├── conf #配置文件
│   ├── __init__.py
│   └── config.py
├── core #主要程序逻辑都 在这个目录 里
│   ├── atm_mod			#atm 操作
│   │	├── __init__.py			
│   │	├── accounts.py			#涉及金钱操作模块
│   │	└── login.py			#登陆模块
│   ├── shopping_mod	#商城 操作
│   │	├── __init__.py			
│   │	├── shopping.py			#购物模块
│   ├── __init__.py
│   ├── atm.py  		#atm 程序运行入口
│   ├── auth.py         #用户认证模块
│   ├── common_func.py  #公共函数
│   ├── logger.py       #日志记录模块
│   └── shopping.py     #商城 程序运行入口
├── db  #用户数据存储的地方
│   ├── accounts   #用户数据
│   ├── file       #文件处理模块
│   ├── mysql	   #sql 处理模块
│   ├── __init__.py
│   ├── account_sample.py #生成一个初始的账户数据 ,把这个数据 存成一个 以这个账户id为文件名的文件,放在accounts目录 就行了,程序自己去会这里找
│   └── handle     #统一处理
├── log #日志目录
│    ├── __init__.py
│    ├── 1234.access.log #所有的交易日志
│    └── 1234.atm.log    #用户访问和操作的相关日志
└── main.py  #程序主入口
```


# 流程：
* 1、生成初始账号
  * python account_sample.py #可自行修改个人用户数据
* 2、执行入口程序
  * python main.py