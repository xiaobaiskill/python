#!/usr/bin/env python
# Auther Jmz
old_age = 23
for i in range(3) :
    input_age = int(input('oldname age:'))
    if input_age > old_age:
        print('think smaller...')
    elif input_age < old_age:
        print('think bingger...')
    else:
        print('yes ,this right')
        break
else :
    print('正常走完执行')