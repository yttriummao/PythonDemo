# coding=utf-8

import urllib.request

response = urllib.request.urlopen("http://www.boc.cn/")
html = response.read()
html = html.decode("utf-8") #注意：这里的编码格式要和第一行的coding一致
print(html)