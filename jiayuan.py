#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from urllib.request import quote


server = "唯我独尊"
map = "广陵邑"
# print(quote(server))
download_header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
url = "https://next.jx3box.com/api/flower/price/rank?server={server}&map={map}"
#print(url.format(server=quote(server),map=quote(map)))
page=requests.get(url.format(server=quote(server),map=quote(map)),headers=download_header).json()
# tree=html.fromstring(page.text)
for i in page:
    print("%s，目前价格%s,线路%s" %(i,page.get(i).get('max'),page.get(i).get('maxLine')))




