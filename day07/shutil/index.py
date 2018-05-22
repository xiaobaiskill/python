#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import shutil

# 1、shutil.copyfileobj(fsrc, fdst[, length])
# 将文件内容拷贝到另一个文件中
#  shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))

# 2、shutil.copyfile(src, dst) #拷贝文件

# 3、shutil.copymode(src, dst) # 仅拷贝权限。内容、组、用户均不变

# 4、shutil.copystat(src, dst) # 仅拷贝状态的信息，包括：mode bits, atime, mtime, flags

# 5、shutil.copy(src, dst) # 拷贝文件和权限

# 6、 shutil.copy2(src, dst) # 拷贝文件和状态信息

# 7、shutil.copytree(src, dst, symlinks=False, ignore=None) #递归的去拷贝文件夹
#   shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
# #目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除


# 8、shutil.rmtree(path[, ignore_errors[, onerror]]) # 递归的去删除文件

# 9、shutil.move(src, dst) # mv 递归的去移动文件，它类似mv命令，其实就是重命名。

# 10、shutil.make_archive(base_name, format,...)
#    base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
#    如 data_bak                       =>保存至当前路径
#    如：/tmp/data_bak =>保存至/tmp/
#    format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
#    root_dir：	要压缩的文件夹路径（默认当前目录）
#    owner：	用户，默认当前用户
#    group：	组，默认当前组
#    logger：	用于记录日志，通常是logging.Logger对象





# 压缩和解压操作
# 压缩
res =shutil.make_archive('a',format='zip')
print(res)


# 解压
import zipfile
z= zipfile.ZipFile('a.zip','r')
z.extractall('./a')
z.close()




