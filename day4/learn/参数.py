#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz









#可变长参数
# 溢出位置实参接受*
# def foo(x,y,*z):
#     print(x,y)
#     print(z)
# foo(1,2,3,4,5)
# foo(1,2,*[3,4,5])    #foo(1,2,3,4,5)
# foo(1,[2,3,4,5])      # [2,3,4,5] 是作为一个整体的实参，有没有用*转化成个体
# foo(1,2,*'abc')       #foo(1,2,'a','b,'c')

# 溢出关键字实参接受**
# def func(x,y,**z):
#     print(x,y)
#     print(z)
#
# func(1,2,a=3,b=4)            #z = {'a':3,'b':4}
# func(z='a',k='k',x=1,y=2)    # z ={'z':'a','k':'k'}
#
# func(1,2,**{'a':3,'b':4})
# func(1,2,**{'k':3,'z':4})

# 约定俗成的定义方式
# *arg  接受所有的溢出位置参数
## **kwargs 接受所有的溢出关键字参数
# def foo(*arg,**kwargs):
#     print(arg)
#     print(kwargs)
#
# foo(1,3,4,*(4,5,6),y='a',z='b',**{'f':'f','k':'k'})




# 练习题;
def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(sum(1,23,4,5))
print(sum(2,3,4,4))

def compare(x,y,z='small'):
    '''
    取两个数的最大或最小值
    :param x:
    :param y:
    :param z: small or big
    :return:
    '''
    if z == 'small':
        return x if x<y else y
    elif z == 'big':
        return x if x > y else y
    else:
        pass

print(compare(1,3))
print(compare(1,3,'big'))