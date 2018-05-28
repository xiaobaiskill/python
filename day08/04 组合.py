#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



# 设计模式的关系： 关联；
# 关联： 组合，聚合


# 运用场景
# 1、学生有生日属性， 但是生日的值来自于 date 模块（模块当作是类）
# 2、当前场景
#




import pickle

class OldboyPeople(object):
    school = 'oldboy'
    def __init__(self,name,age,sex):
        self.name =name
        self.age = age
        self.sex =sex

    def save(self):
        with open('%s'%self.name,'wb') as f:
            pickle.dump(self,f)

class OldboyStudent(OldboyPeople):
    course = []
    def choose_course(self):
        print('chooise_course')


class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level):
        OldboyPeople.__init__(self,name,age,sex)
        self.level = level
    def score(self,name):
        print('改作业')

class course(object):
    def __init__(self,name,price,proid):
        self.name = name
        self.price = price
        self.proid = proid
    def tell_info(self):
        print('''
        name:%s
        price:%s
        proid:%s
        '''%(self.name,self.price,self.proid))



python = course('python',9000,'5mons')
linux = course('linux',4000,'3mons')

stu1 = OldboyStudent('jmz',25,'man')
stu1.course.append(python)
stu1.course.append(linux)

for course in stu1.course:
    course.tell_info()
