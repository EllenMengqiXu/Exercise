#!/usr/bin/env python
# coding:utf8

import  urllib
import urllib.request
import urllib.parse

import json
from bs4 import BeautifulSoup


# get
url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'

request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request, timeout=20)
result = str(response.read(), 'utf-8')

print(result)


# post

url = 'https://shuju.wdzj.com/depth-data.html'
data = urllib.parse.urlencode({'type1': 1, 'type2': 2, 'status': 0, 'wdzjPlatId': 59}).encode("utf-8")
request = urllib.request.Request(url)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
response = urllib.request.urlopen(url, data)
result = response.read()
for key in json.loads(result).keys():
	print(key)
