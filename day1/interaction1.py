#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Auther Jmz
#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Auther Jmz
name =input('name:')
age =input('age:')
obj =input('obj:')

info = '''
---------- info of {_name} --------
name :{_name}
age  :{_age}
obj  :{_obj}
'''.format(_name=name,_age=age,_obj=obj)
print(info)