#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import json

dict = {'name':'jmz','age':23,'sex':'boy','school':{'small_school':'lala','middle_school':'chajj school'}}


with open('json.txt','w',encoding='utf-8') as f:
    f.write(json.dumps(dict))
    # json.dump(dict,f)     # 这是上面的简写


with open('json.txt','r',encoding='utf-8') as f:
    res = json.loads(f.readline())
    # res = json.load(f)        # 上面的简写


print(res['name'])