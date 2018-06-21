#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz

import re
res1 = re.search('(?:batch_run|batch_scp)\s+?-h(.*)?-g(.*)?(?:-cmd|-action)(.*)','batch_run  -h h1,h2,h3   -g web_clusters,db_servers    -cmd  "df -h"')
res2 = re.search('(?:batch_run|batch_scp)\s+?-h(.*)?-g(.*)?(?:-cmd|-action)(.*)','batch_scp   -h h1,h2,h3   -g web_clusters,db_servers  -action put  -local test.py  -remote /tmp/')

print(res1.group(1))
print(res2.group(1))
