#! /usr/bin/env python
# -*- conding:utf-8 -*-
# Author Jmz

# 全局命名空间 x,foo,z
# x= 1
# def foo():
#     print('from foo')
#
# if x ==1:
#     z=3



# 局部命名空间 x,y,z
# def func():
#     x=1
#     y=2
#     z=3
# func()

# len =10
# def f1():
#     len =100
#     def f2():
#         print(len)
#     f2()
# len=11111
# f1()
# x =10
# def f1():
#     print(x)
# def f2():
#     x=1111
#     print(x)
# f1()
# f2()




# 作用域
# x=1
# y=2
# z=3
# # 上面的x,y,z 都是全局
# def foo1():
#     x = 1111     # 在函数内部定义的变量，此时x是局部变量，临时存活
#     def foo2():
#         y=2222    # 这里的y也是局部变量
#         print(x)
#         print(y)
#         print(z)    # 在函数定义，查找关系已经确定，先foo2内，然后foo1然后全局，在该函数调用之前，已创建了一个临时变量z=1000,
#                     # 所以打印1000
#     z=1000
#     foo2()
#     print(y)       # 在foo1 这一层函数内并没有定义临时的局部变量y,所以使用全局y
# foo1()



# global nonlocal



x = 1
def foo():
    x = 2
    def foo2():
        def foo3():
            def foo4():
                nonlocal x    # 使用自己上层作用域内的直至全局作用域内的局部变量
                print(x)   # 2
            foo4()
        foo3()
    foo2()
    print(locals())   # 查看该层的所有的局部变量
foo()
print(globals())      # 查看所有的全局变量

def f1():
    global x     # 使用全局的x
    print(x)   # 1
f1()



