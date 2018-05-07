#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz


#  一、什么是装饰器
    # 1、装饰即修饰，器指的就是工具
    # 2、装饰器本身可以是任意可调用的对象
    # 3、被装饰的对象也可以是任意可调用的对象
#  二、为什么要使用装饰器
    # 1、在不改变原有的调用方式,不改变原方法的前提下，如何实现对内容上的新增？？
    # 例如：
        # 今天公司cto要求对一些方法添加文件的日志记录（此时你是否需要对每一个方法添加日志的记录？）
        # 第二天CTO 突然改变主意说 原来的方法添加日志记录改为 mysql 记录（此时你是否又要改变修改么一个方法的日志记录？？）
        # 我知道你此时此刻一定会想，我可以写一个日志记录方法，让每一个方法内部调用这个方法（很不错的想法）
        # 第三天 你的公司cto 告诉你，我的日志一定要记录那些方法执行的开始和结束时间。（是不是有点懵X了？你该怎么办？？）

#  三、怎么用
    # 是否是和上面的那个闭包函数很像呀（其实装饰器就是闭包函数的一种运用）
    # 装饰器语法糖：
    # 在被装饰对象的正上方一行写@装饰器的名字
    # @auth   ==> func = auth(func)

# 四、有参装饰器
    # 上面的装饰器只是使用了固定的用户jmz,登录，而且没有实现以哪种方式 验证（文件方式，还是mysql方式）
    # 如果我需要暂时以文件的方式验证，后期再改为使用mysql 方式验证该如何使用？？？ （尽量减少代码的修改）
    # 要求：
        # 1、验证的方式是不固定的
        # 2、使用的装饰器要兼顾至少两种以上的验证方式
        # 3、需要能够随时给方法添加验证或撤销验证

# 一：
# login_status = {
#     'user':None,
#     'status':None
# }
#
#
# def login(user:str,pwd:str):
#     if user == 'jmz' and pwd =='123':
#         return True
#     else:
#         return False
#
# # 认真用户是否登录成功
# def auth(func):
#     def wrapper(*args,**kwargs):
#         if login_status['user'] and login_status['status']:
#             return func(*args,**kwargs)
#         else:
#             uname = input('username>>').strip()
#             upwd = input('password>>').strip()
#             res =login(uname,upwd)
#             if res:
#                 return func(*args, **kwargs)
#             else:
#                 print('认证失败')
#     return wrapper
#
#
#
# def index():
#     print('from index')
#
# index = auth(index)
#
# def cat():
#     print('form cat')
#
# index()
# cat()

# 三：
# login_status = {
#     'user':None,
#     'status':None
# }
#
# def login(user:str,pwd:str):
#     if user == 'jmz' and pwd =='123':
#         login_status['user']=user
#         login_status['status']=True
#         return True
#     else:
#         return False
#
# # 认证用户是否登录成功
# def auth(func):
#     def wrapper(*args,**kwargs):
#         if login_status['user'] and login_status['status']:
#             return func(*args,**kwargs)
#         else:
#             uname = input('username>>').strip()
#             upwd = input('password>>').strip()
#             res =login(uname,upwd)
#             if res:
#                 return func(*args, **kwargs)
#             else:
#                 print('认证失败')
#     return wrapper
#
#
# @auth
# def index():
#     print('from index')
#
# @auth
# def cat():
#     print('form cat')
#
# index()
# cat()




# 四：
login_status = {
    'user':None,
    'status':None
}

def login(user:str,pwd:str,type='file'):
    if type == 'file':
        # 假设这就是文件认证
        if user == 'jmz' and pwd == '123':
            login_status['user'] = user
            login_status['status'] = True
            return True
        else:
            return False
    elif type =='mysql':
        # 假设这就是mysql认证
        if user == 'jmz' and pwd == '123':
            login_status['user'] = user
            login_status['status'] = True
            return True
        else:
            return False



# 认证用户是否登录成功
def auth(type='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            if login_status['user'] and login_status['status']:
                return func(*args,**kwargs)
            else:
                uname = input('username>>').strip()
                upwd = input('password>>').strip()
                res =login(uname,upwd,type)
                if res:
                    return func(*args, **kwargs)
                else:
                    print('认证失败')
        return wrapper
    return auth2


@auth('file')
def index():
    print('from index')

@auth('file')
def cat():
    print('form cat')

index()
cat()





