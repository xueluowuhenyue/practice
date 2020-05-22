# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://book.zongheng.com/chapter/806206/46469475.html'
# 1. 先构建一个字典
header={"user-agent":"Mozilla/5.0"}
res = requests.get(url, headers=header)
res.encoding=res.apparent_encoding          # 修改为解析的编码
bf=BeautifulSoup(res.text)
texts=bf.find_all('div',class_="content")
# print(texts)
print(texts[0].text.replace('\xa0'*8,'\n\n'))