#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import requests,os,hashlib
cache_file = 'cache.txt'
engine_settings={
    'file':{'dirname':'db'},
    'mysql':{
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'password':'123'
    },
    'redis':{
        'host':'127.0.0.1',
        'port':6379,
        'user':'root',
        'password':'123'
    }
}
def make_cache(type = 'file'):
    def deco(func):
        def wrapper(url):
            if type == 'file':
                cache_filename = 'aa'
                # cache_filename = m.hexdigest()
                cache_filepath = r'%s/%s'%(engine_settings['file']['dirname'],cache_filename)
                if os.path.exists(cache_filepath) and os.path.getsize(cache_filepath):
                    return open(cache_filepath,encoding='utf-8').read()
                res = func(url)
                with open(cache_filepath,'w',encoding='utf-8') as f_new:
                    f_new.write(res)
                return res
            elif type == 'redis':
                pass
            elif type == 'mysql':
                pass
            else:
                pass
        return wrapper
    return deco

@make_cache()
def geturl(url):
    return requests.get(url).text

print(geturl('https://www.baidu.com'))


