#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author Jmz
import sys
from conf.settings import BASE_DIR

from core import src

sys.path.append(BASE_DIR)

src.run()


