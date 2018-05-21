#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


import time

# print('\r[#          ]',end='')
# time.sleep(0.3)
# print('\r[###        ]',end='')
# time.sleep(0.3)
# print('\r[#######    ]',end='')
# time.sleep(0.3)
# print('\r[###########]',end='')

# x = 0
# while x <= 50:
#     print('\r[%-50s] %d%%'%(x*'#',x//50*100),end='')    # %-50s  表示总共50个字符，不足以空格补充
#     x+=10
#     time.sleep(0.3)


def proccess(x,width=40):
    if x > 1:
        x =1
    pro_format = ('[%%-%ds]'%width) %(int(x*width)*'#')  # '%%' 表示%
    res = '%s %d%%'%(pro_format,int(x*100))
    print('\r %s'%res,end='')

start =0
total = 10484
while start <= total:
    start += 1024
    proccess(start/total)
    time.sleep(0.3)



# 补充知识点 1
#   在windows 中 \r 表示光标移动至行首， \n 跳到下一行，光标不变
#   linux \n 表示就是\r\n


# 补充知识点2
#   %-30s 表示共30个字符，不足以空格补充
#   %% 表示%， 因为格式化操作 % 有特殊意义
#   ('[%%-%ds]'%10)%('###')   ===> '[%-10s]'%('###')   ===> [###       ]


