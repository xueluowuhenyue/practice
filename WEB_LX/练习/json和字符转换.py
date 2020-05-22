# -*- coding:utf-8 -*-
# import json
# s='{"name":"小明","age":"18"}'
# d={"name":"小明","age":"18"}
#
# # 字符串转字典 loads
# print(type(json.loads(s)))
# # 字典转字符串 dumps
# print(json.dumps(d,ensure_ascii=False))

from selenium.webdriver import Chrome
import requests
from selenium.webdriver.common.by import By

driver=Chrome(executable_path=r'C:\python35\Scripts\chromedriver.exe',port=6666)
# Command.GET: ('POST', '/session/$sessionId/url')
session_id= driver.session_id
url='http://localhost:6666/session/{}/url'.format(session_id)
bai_url = 'http://www.baidu.com'
dict = {'url': bai_url}
requests.post(url,json=dict)
# 定位元素
session_id=driver.session_id
url="http://localhost:6666/session/{}/url".format(session_id)
# 定位输入框
data={'using':By.CSS_SELECTOR,'value':'#kw'}
# 获取请求结果
res=requests.post(url,json=data)

# 输入搜索字符
session_id=driver.session_id
# url="http://localhost:6666/session/{}/element/{}/value".format(session_id,'kw')
# 获取请求结果
data={'volue': 'python'}
res=requests.post(url,json=data)
print(res.json())
# ('POST', '/session/$sessionId/element/$id/value')


# 获取标题
# session_id=driver.session_id
# url="http://localhost:6666/session/{}/title".format(session_id)
# res=requests.get(url)
# d=res.json()
# print(d["value"])
# {"sessionId":"8727c95ade46b5fcd009218240cf6523","status":0,"value":"百度一下，你就知道"}
