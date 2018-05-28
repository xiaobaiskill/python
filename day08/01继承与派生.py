#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

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
    def choose_course(self):
        print('chooise_course')


class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level):
        OldboyPeople.__init__(self,name,age,sex)
        self.level = level
    def score(self,name):
        print('改作业')



stu1 = OldboyStudent('jmz',25,'man')
stu1.save()



tea1 = OldboyTeacher('egon','18','man',10)
tea1.save()