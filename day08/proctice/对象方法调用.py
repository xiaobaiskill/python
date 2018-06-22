#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


class student():   # 定义类
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def learn(self,object):          # 定义类方法，参数object， 课程
        print('%s 正在学习 %s 中'%(self.name,object))

wdp = student('王大炮',23)   #实例化产生对象，赋值给wdp，此时wdp 继承了类的方法和属性
print(wdp.__dict__)   #查看对象属性
# {'name': '王大炮', 'age': 23}
wdp.learn('英语')             # 调用 对象方法
# 王大炮 正在学习 英语 中



ltg = student('李坦克',33)
# 类方式调用时是需要传入self参数的，对象不需要
student.learn(ltg,'历史')    # 此方式与 ltg。learn('历史') 结果一样。
# 李坦克 正在学习 历史 中

