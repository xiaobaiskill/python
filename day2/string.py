#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther Jmz

# \t 表示tab键
context = "my\t namE is 淡粉色的 jmz and {name}"
print(context)

print(context.capitalize())            # 首字母大写

print(context.count('m',1,-1))              # 查找 m有多少个 从第1个下标开始。 到倒数第1个一共有2个m    区分大小写的
print(context.count('m',1,7))               # 从下标为1到 小标为7结束， 包头不包尾

print(context.casefold())              # 3.3 之后引入的，大写转小写

print(context.center(50,'+'))          # 将内容放至中间，两边以'+' 显示，共50个

print(context.encode('utf-8'))
print(context.encode('utf-8').decode(encoding='utf-8'))

print(context.endswith('jmz'))           # 什么结尾，如果以jmz结尾则为true，不是则为false
print(context.expandtabs(40))            #将tab 以 40个空字符串表示

print(context.find('n',1,5))                 # 返回查找到的字符串的开始下标     -1 表示没有找到       包头不包尾的原则

print(context[2:9])                          # 也只能这样切片 了

print(context.format(name='qqc'))              # 格式化
print(context.format_map({'name':'qqc'}))      # 字典
print(context.index('na'))                     # 与find 差不多 。也是查找返回下标  。  没有的话就不显示

print(context.isalnum())                        # 判断是否是阿拉伯字符 即a-z0-9  数字.也不行
print('a23'.isalnum())


print('---------start ------')
print('16.66'.isdecimal())                     # 只能 Unicode数字，，全角数字（双字节）
print('五'.isdigit())                       # 数字就行了，不能是汉子数字
print('1313'.isnumeric())                   # Unicode数字，全角数字（双字节），罗马数字，汉字数字  不支持byte数字（单字节）
print('-------end---------')


print('mynamEis淡粉色的jmzand'.isidentifier())               # 是否可作为一个合法的变量名

print('dsadas'.islower())                    # 是否都是小写

print(' '.isspace())                            # 是否是一个空格

print('My Name Is '.istitle())                  # 单词首字母大写
print('My Name Is '.isprintable())              # 是否可以打印的。 一般无需使用  tty file ,diver file   之类的无法打印
print('MY NAME  IS '.isupper())                # 判断是否全为大写

print(','.join(['1','2','3']))                 # 元组必须是字符串型   以',' 分割

print('My Name Is '.ljust(50,'*'))             # 长度50，不够向右以*不补足

print('My Name Is '.rjust(50,'*'))              # 长度50，不够向左以*不补足

print('-------1111---------')
print('My name IS'.lower())                     # 大写转小写

print(' my name IS '.upper())                    # 小写转大写

print(' my name IS \n'.lstrip())                    # 去除左边的空格回车  lsstrip
print(' my name IS     \n   '.rstrip())             # 去除右边的空格回车
print('      my name IS     \n   '.strip())         # 去除两边的空格回车
print('-----------22222---------')


p= str.maketrans('abcdef','123456')                # 多数用在 密码转化上面
print('i am abc'.translate(p))                     # 就是数字对应转化

print('-----------333---------')

print(' jmz-666 '.replace('6','9',2))              # 6 替换成9 只替换2个

print('jmz-666-dsz'.rfind(''))                    # 返回最右边的 查找到的下标   没找到为 -1

print('xiao bai skill'.split('b'))                   # 将字符串以切割成列表。 默认是以' '切割

print('xiao bai\r skill'.splitlines())               # 以换行做切割   看不出有什么作用

print('My Name IS XIAOBAISKILL'.swapcase())          # 大小写身份转化

print('my name is xiaobaiskill'.title())            #单词首字母大写

print('my NAme Is Xiaobaiskill'.upper())            # 小写转大写

print('my NAme Is Xiaobaiskill'.lower())            # 大写转小写

print('my name is xiaobaiskill'.zfill(50))          # 自动补全前面为0
