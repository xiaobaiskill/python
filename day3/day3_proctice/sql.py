#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz


# 字段仅存在
# staff_id,name.age,phone,dept,enroll_date


# insert
# insert [into] <表名> (列名) values (列值)
#   insert into emp(name,age,phone) value('jmz11111',23,182553342632)
#   insert into emp values('金明智',23,'182551832632','开发'),('jmz',23,'18326323334','开发')
#   insert into emp('name','phone',dept) values('aaa','182521832632','开发'),('jmz','13326323334','开发')

#delete
#delete from <表名> [where <删除条件>]
#   delete from emp where name =2
#   delete from emp where name =2 and id =2
#   delete from emp where name like '金明智' and age =23 or  staff_id =1


# update
# update <表名> set <列名=更新值> [where <更新条件>]
#   update emp set name = 'jmz1111' where staff_id =1
#   update emp set name=jjj,age=23 where staff_id<5 or name like jmz and staff_id>25


#select
# select <列名> from <表名> [where <查询条件表达试>] [order by <排序的列名>[asc或desc]] [limit <取值>]
#   select * from emp where staff_id >4 and name like 'jmz'
#   select * from emp where staff_id>25
#   select name,age,phone from emp where staff_id >4 and name like 'jmz'



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
    result = re.match('\s*?update\s+?(\w+)\s+?set\s+?(.*?)\s*?(where(.*))?$',sql)
    if result:
        sql_dict['table'] =result.group(1)
        if result.group(2):
            values = result.group(2);
            values_list=values.split(',')
            for value in values_list:
                key_value=value.split('=')
                if len(key_value) ==2:
                    kye_values={key_value[0].strip(' \'\"'):key_value[1].strip(' \'\"')}
                    sql_dict['values'].update(kye_values)
                else:
                    return
        else:
            return
        if result.group(4):
            sql_dict['where'] = where_parse(result.group(4))
    return sql_dict

def parse_select(sql):
    sql_dict = {
        'type': 'select',
        'table': '',
        'filed': {},
        'where': []
    }
    result = re.match('\s*?select\s+?(.*)\s+?from\s+?(.*?)\s*?(where(.*))?$', sql)
    if result:
        if result.group(2):
            sql_dict['table'] = result.group(2)
        else:
            return
        if result.group(1):
            sql_dict['filed'] = result.group(1).split(',')
        else:
            return
        if result.group(4):
            sql_dict['where'] = where_parse(result.group(4))
    else:
        return
    return sql_dict

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
                    max_id =0
                    with open(command['table'],'r',encoding='utf-8') as f:
                        for line in f:
                            line_values = line.split(',')
                            if 'phone' in key_values.keys():
                                if key_values['phone']  == line_values[3]:
                                    print('phone:%s 已存在不可添加'%key_values['phone'])
                                    return
                            else:
                                print('缺少唯一索引：phone')
                                return
                            if max_id < int(line_values[0]):
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

def update_action(command):
    '''
    修改操作
    :param comand:
    :return:
    '''
    if command['table']:
        if command['values']:
            with open(command['table'],'r',encoding='utf-8') as f:
                for line in f:
                    line_list = line.split(',')
                    line_dict = {
                        'staff_id': line_list[0],
                        'name': line_list[1],
                        'age': line_list[2],
                        'phone': line_list[3],
                        'dept': line_list[4],
                        'enroll_date': line_list[5].strip()
                    }
                    for k,v in command['values'].items():
                        if k in line_dict.keys():
                            if (command['where'] and where_action(command['where'],line)) or not command['where']:
                                line_dict[k]=v
                        else:
                            print('%s:表字段不存在'%k)
                            return
                    with open('%s.swap'%(command['table']),'a',encoding='utf-8') as f_new:
                        f_new.write('%s\n'%','.join(line_dict.values()))

            os.remove(command['table'])
            os.rename('%s.swap'%command['table'],command['table'])

            print('update successful')
        else:
            print('无可修改数据')
    else:
        print('无可修改对象')

def select_action(command):
    '''
    查操作
    :param comand:
    :return:
    '''
    if command['table']:
        with open(command['table'], 'r', encoding='utf-8') as f:
            for line in f:
                line_list = line.split(',')
                line_dict = {
                    'staff_id': line_list[0],
                    'name': line_list[1],
                    'age': line_list[2],
                    'phone': line_list[3],
                    'dept': line_list[4],
                    'enroll_date': line_list[5].strip()
                }
                if command['where']:
                    if where_action(command['where'], line):
                        if command['filed'][0] == '*':
                            print(line.strip())
                        else:
                            filed_values = []
                            for filed in command['filed']:
                                if filed in line_dict.keys():
                                    filed_values.append(line_dict[filed])
                                else:
                                    print('%s:字段不存在'%filed)
                                    return
                            print(','.join( filed_values))
                else:
                    if command['filed'][0] == '*':
                        print(line.strip())
                    else:
                        filed_values = []
                        for filed in command['filed']:
                            if filed in line_dict.keys():
                                filed_values.append(line_dict[filed])
                            else:
                                print('%s:字段不存在' % filed)
                                return
                        print(','.join(filed_values))
        print('select successful')
    else:
        print('无可查找对象')

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
        return int(line_dict[key]) > int(value[0])
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
    if sql =='q':
        print('sql退出')
        break
    sql_parse_result = sql_parse(sql)
    if sql_parse_result:
        if os.path.exists(sql_parse_result['table']):
            sql_result = sql_action(sql_parse_result)
        else:
            print('数据库操作对象不存在')
    else:
        print('SQL语句有误')


