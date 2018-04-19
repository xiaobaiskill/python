#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

# insert
# insert [into] <表名> (列名) values (列值)
#   insert into emp values('金明智',23,'182551832632','开发'),('jmz',23,'18326323334','开发')
#   insert into emp('name','phone',dept) values('aaa','182521832632','开发'),('jmz','13326323334','开发')

#delete
#delete from <表名> [where <删除条件>]
#   delete from emp where name =2
#   delete from emp where name =2 and id =2
#   delete from emp where name like '金明智' and age =23 or  staff_id =1


# update
# update <表名> set <列名=更新值> [where <更新条件>]
# update emp set name='jmz' where staff_id =2

#select
# select <列名> from <表名> [where <查询条件表达试>] [order by <排序的列名>[asc或desc]] [limit <取值>]


import re,time,os

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
        return sql_type[sql_list[0]](sql)


def parse_insert(sql):
    sql_dict = {
        'type':'insert',
        'table':'',
        'keys':[],
        'values':[]
    }
    sql_list = sql.split(' ')
    if 'into' in sql_list:
        result = re.match('(\w+)\s*?(\(.+\))?',sql_list[sql_list.index('into')+1])
        if result:
            sql_dict['table'] = result.group(1)
            if result.group(2):
                keys_before = result.group(2).strip('() ').split(',')
                for key in keys_before:
                    sql_dict['keys'].append(key.strip('\'\" '))
    if 'values' in sql:
        values_before_str = sql.split('values')[1]
        values_before_result = re.match('\((.+?)\)',values_before_str)
        if values_before_result:
            regex = re.compile('\((.+?)\)')
            for values_before in regex.findall(values_before_str):
                values = []
                for value_before in values_before.split(','):
                    values.append(value_before.strip('\'\" '))
                sql_dict['values'].append(values)
    elif 'value' in sql:
        values_before = sql.split('value')[1].strip('() ').split(',')
        values = []
        for value_before in values_before:
            values.append(value_before.strip('\'\" '))
        sql_dict['values'].append(values)
    return sql_dict

def parse_delete(sql):
    sql_dict = {
        'type':'delete',
        'table':'',
        'where':[]
    }
    if 'from' in sql:
        result = re.match('\s*?delete\s+?from\s+?(\w+)(\s+?where(.*))?',sql)
        if result :
            sql_dict['table'] =result.group(1)
            if result.group(3):
                result_where = where_parse(result.group(3))
                if result_where:
                    sql_dict['where'] = result_where
                else:
                    return
        return sql_dict

def parse_update(sql):
    sql_dict = {
        'type':'update',
        'table':'',
        'values':{},
        'where':[]
    }
    result = re.match('\s*?update(.*?)set(.*?)(where(.*))?',sql)
    print(result.groups())
    if result:
        sql_dict['table'] =result.group(1)
        if result.group(2):
            pass
        else:
            return

    pass

def parse_select(sql):
    return 'select'
    pass


def where_parse(sql_where):
    '''
    where 的解析
    :param sql_where: where 后面的sql 语句
    :return: {'and':[{}]}  {'or':[{},{},{}]}
    '''
    def one_parse_where(sql_one_where):
        result = re.match('\s*?(\w+)\s*?(>|<=|<|>=|=|like)\s*?[\'|\"]?(\w+)[\'|\"]?',sql_one_where)
        if result :
            return {result.group(1):[result.group(3),result.group(2)]}
    def and_where_parse (and_sql_where):
        and_where = {}
        if 'and' in and_sql_where.strip('() '):
            and_sql_where_list = and_sql_where.split('and')
            for and_sql_where_value in and_sql_where_list:
                result_one_sql = one_parse_where(and_sql_where_value.strip('() '))
                if result_one_sql:
                    and_where.update(result_one_sql)
                else:
                    return
        else:
            result_one_sql = one_parse_where(and_sql_where.strip('() '))
            if result_one_sql:
                and_where.update(result_one_sql)
            else:
                return
        return and_where

    where = {}
    if 'or' in sql_where:
        sql_where_list = sql_where.strip().split('or')
        where['or']=[]
        for sql_where_value in  sql_where_list:
            result_sql_where = and_where_parse(sql_where_value)
            if result_sql_where:
                where['or'].append(result_sql_where)
            else:
                return
    else:
        result_sql_where=and_where_parse(sql_where)
        if result_sql_where:
            where['and']=result_sql_where
        else:
            return
    return where



def sql_action(command):
    '''
    sql 代码执行
    :param sal [list]:
    :return:
    '''
    sql_action_dict={
        'insert':insert_action,
        'delete':delete_action,
        'update':update_action,
        'select':select_action
    }
    sql_type = command['type']
    command.pop('type')
    return sql_action_dict[sql_type](command)


def insert_action(command):
    '''
    insert 语句执行
    :param command:
    :return:
    '''
    if command['table']:
        if not command['keys']:
            command['keys'] = ['name','age','phone','dept']
        else:
            for filed in command['keys']:
                if filed not in ['name','age','phone','dept']:
                    print('%s 字段不存在'%(filed))
                    return
        if command['values']:
            for values in command['values']:
                len_keys = len(command['keys'])
                if len(values) == len_keys:
                    key_values={}
                    i = 0
                    for key in command['keys']:
                        if key in ['name','age','phone','dept']:
                            key_values[key] = values[i]
                        i+=1
                    with open(command['table'],'r',encoding='utf-8') as f:
                        for line in f:
                            line_values = line.split(',')
                            if 'phone' in key_values.keys():
                                if key_values['phone']  == line_values[3]:
                                    print('phone:%s 已存在不可添加'%key_values['phone'])
                                    break
                            else:
                                print('缺少唯一索引：phone')
                                return
                            max_id = int(line_values[0])
                    with open(command['table'], 'a', encoding='utf-8') as f_add:
                        f_add.write('%d,%s,%s,%s,%s,%s\n'%(max_id+1,key_values['name'] if 'name' in key_values.keys() else '',\
                                                         key_values['age'] if 'age' in key_values.keys() else '', \
                                                           key_values['phone'] if 'phone' in key_values.keys() else '', \
                                                           key_values['dept'] if 'dept' in key_values.keys() else '', \
                                                           time.strftime("%Y-%m-%d", time.localtime())))
                else:
                    print('insert:指定的键与值不统一')
                    return
            print('insert successful')

def delete_action(command):
    '''
    删除操作
    :param comand:
    :return:
    '''
    if command['table']:
        if command['where']:
            with open(command['table'],'r',encoding='utf-8') as f:
                for line in f:
                    if not where_action(command['where'],line):
                        with open('%s.swap'%(command['table']),'a',encoding='utf-8') as f_new:
                            f_new.write(line)
            os.remove(command['table'])
            os.rename('%s.swap'%command['table'],command['table'])
        else:
            os.remove(command['table'])
            f=open(command['table'],'w',encoding='utf-8')
            f.close()
        print('delete successful')
    else:
        print('无可删除对象')

def select_action(commnd):
    pass

def update_action(command):
    pass

def where_action(where,line):
    '''
    条件是否成立
    :param where:  {'and':[{key:[value,operation]}]}  {'or':[{},{},{}]}
    :param line: 1,姬建明,25,15201541043,运维,2013-11-01
    :return: boolean
    '''
    line_list = line.split(',')
    line_dict = {
        'staff_id': line_list[0],
        'name': line_list[1],
        'age': line_list[2],
        'phone': line_list[3],
        'dept': line_list[4]
    }
    if 'or' in where.keys():
        for key in where['or']:
            if and_where_action(key,line_dict):
                return True
    else:
        if and_where_action(where['and'], line_dict):
            return True
    return False

def and_where_action(and_where_dict,line_dict):
    for k,v in and_where_dict.items():
        if k not in line_dict.keys():
            return False
        if not operation(k,v,line_dict):
            return False
    return True

def operation(key,value,line_dict):
    if value[1] == '>=':
        return int(line_dict[key]) >= int(value[0])
    elif value[1] == '>':
        return int(line_dict[key]) < int(value[0])
    elif value[1] == '<=':
        return int(line_dict[key]) <= int(value[0])
    elif value[1] == '<':
        return int(line_dict[key]) < int(value[0])
    elif value[1] == '=':
        return line_dict[key] == value[0]
    elif value[1] == 'like':
        return value[0] in line_dict[key]
    return False

while True:
    sql = input('sql>>')
    sql = sql.strip().lower()
    sql_parse_result = sql_parse(sql)
    if sql_parse_result:
        print(sql_parse_result)
        sql_result = sql_action(sql_parse_result)
    else:
        print('SQL语句有误')


