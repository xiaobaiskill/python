#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# 定义
class OldboyStudent:
    school='oldboy'
    def select_obj(self):
        print('l select object')

    # print('=====>')


# OldboyStudent.__dict__['select_obj'](123)
#
# print(OldboyStudent.school)
# OldboyStudent.name = 'jmz'      # 增加 元素
# print(OldboyStudent.__dict__)
# del OldboyStudent.school        # 删元素
# print(OldboyStudent.__dict__)

def init(obj, name, age, sex):
    obj.name = name
    obj.age = age
    obj.sex = sex



# 调用类，创建了一个对象
stu1 = OldboyStudent()
stu2 = OldboyStudent()
stu3 = OldboyStudent()


init(stu1,'jmz','23','man')
init(stu2,'ddd','18','man')
init(stu3,'aaa','63','girl')


print(stu1.__dict__)
print(stu2.__dict__)
print(stu3.__dict__)


# 对象的属性方法的查找顺序是先从对象自己的名称空间中查找，再从类中找
print(stu1.school,id(stu1.school))
print(stu2.school,id(stu2.school))
print(stu3.school,id(stu3.school))







