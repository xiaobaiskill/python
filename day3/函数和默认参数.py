#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 默认参数
# 注意事项：
#   1、 位置参数要写在前面
#   2、 位置参数也可用关键参数表示，但一定符合1的原则


def stu_info(name,age,country='china',object='PY'):
    print('学生信息'.center(50,'-'))
    print('学生姓名：',name)
    print('学生年龄：',age)
    print('学生国籍：',country)
    print('学生课程：',object)


# 'jmz',24即为name,age 的位置参数
stu_info('jmz',24)

# xiaobaiskll 为位置参数，country ='USA',age=25  这些是关键参数
stu_info('xiaobaiskill',country='USA',age=25)


