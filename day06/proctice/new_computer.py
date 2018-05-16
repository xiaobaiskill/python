#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import re

def computer_mul_div(expressions):
    '''
    乘除操作
    :param 数学公式:
    :return:
    '''
    pattern = '\d+\.?\d*[\*\/][\-]?\d+\.?\d*'
    if not re.search(pattern,expressions):
        return expressions
    else:
        result = re.search(pattern,expressions).group()
        if len(result.split('*')) > 1:
            n1, n2 = result.split('*')
            value = float(n1) * float(n2)
        else:
            n1, n2 = result.split('/')
            value = float(n1) / float(n2)

        before, after = re.split('\d+\.?\d*[\*\/][\-]?\d+\.?\d*', expressions, 1)
        expressions = '%s%s%s' % (before, value, after)
        return computer_mul_div(expressions)


def computer_add_minus(expressions):
    '''
    加减操作
    :param 数学公式:
    :return:
    '''
    pattern = '[\-\+]?\d+\.?\d*[\+\-]\d+\.?\d*'
    expressions = re.sub('\+\+', '-', expressions)
    expressions = re.sub('\+\-', '-', expressions)
    expressions = re.sub('\-\+', '-', expressions)
    expressions = re.sub('\-\-', '+', expressions)

    if not re.search(pattern,expressions):
        return expressions
    else:
        result = re.search(pattern, expressions).group()
        result = result.lstrip('+')
        if len(result.split('+')) > 1:
            n1, n2 = result.split('+')
            value = float(n1) + float(n2)
        else:
            n1, n2 = result.rsplit('-', 1)
            value = float(n1) - float(n2)

        before, after = re.split(pattern, expressions, 1)
        expressions = '%s%s%s' % (before, value, after)
        return computer_add_minus(expressions)


def computer(expressions):
    '''
    加减乘除
    :param 数学公式:
    :return:
    '''
    expressions = computer_mul_div(expressions)
    expressions = computer_add_minus(expressions)
    return expressions



def exec_computer(expressions):
    '''
    特殊字符处理
    :param 不含空格的数学公式:
    :return:
    '''
    pattern = '\([^\(]*?\)'
    if not re.search(pattern,expressions):
        return computer(expressions)
    else:
        result = re.search(pattern,expressions).group()
        value = computer(result.strip('()'))
        before, after = re.split('\([^\(]*?\)', expressions, 1)
        expressions = '%s%s%s' % (before, value, after)
        return exec_computer(expressions)




if __name__ == '__main__':
    # expression1='1-2*((60+2*(-3-(40.0)/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
    # expression = expression1.replace(' ','')

    # expression2 = '2+3*(9/3)'
    # expression = expression2.replace(' ','')

    expression3 = '-2+3'
    expression = expression3.replace(' ','')

    print(exec_computer(expression))
    print('eval:%s'%eval(expression))