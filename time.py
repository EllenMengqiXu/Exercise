#!/usr/bin/env python
# coding:utf8

import time
localtime = time.time()
print (localtime)

import datetime
lt=datetime.datetime.fromtimestamp(localtime).strftime('%Y-%m-%d %H:%M:%S')
print(lt)
