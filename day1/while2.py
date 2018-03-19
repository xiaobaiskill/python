#!/usr/bin/env python
# Auther Jmz
old_age = 23
count = 0
while count < 3:
    input_age = int(input('oldname age:'))
    if input_age > old_age:
        print('think smaller...')
    elif input_age < old_age:
        print('think bingger...')
    else:
        print('yes ,this right')
        break
    count += 1
    if count == 3 :
        guess = input('Do you want to guess?[y|n]')
        if guess != 'n' :
            count = 0
else:
    print('game over ')