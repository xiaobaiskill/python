#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


class atm(object):
    def __init__(self,user):
        pass

    @classmethod
    def register(sls,user,pwd):
        pass

    @classmethod
    def login(cls,user,pwd):
        pass

    def withdraw(self,money):
        '''
        提现
        :return:
        '''
        pass

    def transfer(self,user,money):
        '''
        转帐
        :param user:
        :param money:
        :return:
        '''
        pass

    def loging(self):
        '''
        atm 操作记录
        :return:
        '''
        pass

    def cat_log(self):
        '''
        查看atm 操作记录
        :return:
        '''
        pass

    def cat_account(self):
        '''
        查看消费流水
        :return:
        '''
        pass






class shopping(object):
    def add_shopping(self):
        '''
        添加商品
        :return:
        '''
        pass

    def cat_good(self):
        '''
        查看商品    # 就简原则，应该有一个商品类的
        :return:
        '''
        pass

    def cat_shopping(self):
        '''
        查看要购买商品
        :return:
        '''
        pass

    def bug(self):
        '''
        购买商品
        :return:
        '''
        pass