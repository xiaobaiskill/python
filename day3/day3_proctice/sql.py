#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# insert
# insert [into] <表名> (列名) values (列值)

#delete
#delete from <表名> [where <删除条件>]

# update
# update <表名> set <列名=更新值> [where <更新条件>]

#select
# select <列名> from <表名> [where <查询条件表达试>] [order by <排序的列名>[asc或desc]] [limit <取值>]


import re

def sql_parse(sql):
    '''
    sql 语句解析
    :param sql语句 :
    :return: 返回 指定语句类型
    '''
    sql_type={
        'insert':parse_insert,
        'delete':parse_delete,
        'update':parse_update,
        'select':parse_select
    }
    sql_list = sql.split(' ')
    if sql_list[0] in sql_type.keys():
        return sql_type[sql_list[0]](sql_list)
    else:
        return

def parse_insert(sql_list):
    sql_dict = {
        'table':'',
        'keys':[],
        'values':{}
    }
    if 'into' in sql_list:
        result = re.match('(\w+)\s*?(\(.+\))?',sql_list[sql_list.index('into')+1])
        if result:
            sql_dict['table'] = result.group(1)
            if result.group(2):
                sql_dict['keys']=result.group(2).strip('() ').split(',')
    if 'values' in 
    return 'insert'
    pass
def parse_delete(sql):
    result = re.match('delete\s+?from\s+?(\w+)(\s+?where(.*))?',sql)
    parse = dict()
    if result:
        parse['table'] = result.group(1)
        if result.group(2):
            parse['where'] = result.group(3)
    return parse
def parse_update(sql):
    return 'update'
    pass
def parse_select(sql):
    return 'select'
    pass





def sql_action(command):
    '''
    sql 代码执行
    :param sal [list]:
    :return:
    '''
    pass

def insert_action(command):
    pass
def select_action(commnd):
    pass
def update_action(command):
    pass
def delete_action(aommand):
    pass

while True:
    sql = input('sql>>')
    sql = sql.strip().lower()
    sql_type = sql_parse(sql)
    if sql_type:
        parse_resul = globals().get('parse_%s'%sql_type)(sql)
        print(parse_resul)

    # action_result = sql_action(parse_result)


