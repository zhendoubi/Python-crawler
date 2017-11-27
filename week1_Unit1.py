#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
r = requests.get('http://www.baidu.com')
r.status_code
r.encoding = 'utf-8'
print(r.text)