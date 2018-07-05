#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz



def sum(count):
    if count == 1:
        return 100
    return sum(count-1) + 20

print(sum(5))

# 图解
'''
sum(5)  == sum(4) +20
sum(4)  == sum(3) + 20
sum(3)  == sum(2) + 20
sum(2)  == sum(1) + 20
sum(1) == 100
'''


# 递归总结
# 1、 有可以明确地结束条件
# 2、每次进入更深一层递归是，问题规模相比上次递归都应有所减少
# 3、递归效率不高，递归层次过多会导致栈溢出


#python中的递归
# python中的递归效率低，需要在进入下一次递归时保留当前的状态，在其他语言中可以有解决方法：尾递归优化，即在函数的最后一步（而非最后一行)调用自己，尾递归优化：http://egon09.blog.51cto.com/9161406/1842475
# 但是python又没有尾递归，且对递归层级做了限制