# -*- encoding: utf8-*-

import requests

url = "https://www.ptt.cc/index.html"
result = requests.get(url)
result.encoding = 'utf-8'
print (result.text)
