#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

class foo():
    def __init__(self):
        pass
    @classmethod
    def get_instance(cls):  # cls == foo
        if not hasattr(cls,"instance"):
            cls.instance = cls()
        return cls.instance


# 单例模式 ， 只实例化一次
obj1 = foo.get_instance()
obj2 = foo.get_instance()
print(obj1,obj2)
# 两次实例化结果一样，说明只实例化一次

# --------上下对比--------
obj_x = foo()
obj_y = foo()
print(obj_x,obj_y)
# 两个实例化结果不一样


