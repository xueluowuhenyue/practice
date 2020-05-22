from time import sleep
import requests
import logging
from WEB_LX.selenium原理.fenge import get_value

# logging.basicConfig(level=logging.DEBUG)

base_url="http://127.0.0.1:9515/session"

params={'capabilities': {
             'firstMatch': [{}],
             'alwaysMatch': {'browserName': 'chrome',
                             'platformName': 'any',
                             'goog:chromeOptions': {'extensions': [], 'args': []}
                             }},
           'desiredCapabilities': {'browserName': 'chrome',
                                   'version': '',
                                   'platform': 'ANY',
                                   'goog:chromeOptions': {'extensions': [], 'args': []}}
           }

res=requests.post(base_url,json=params)
# print(res.json())
session_id=res.json()['value']['sessionId']
# print(session_id)
logging.debug(msg='='*10+'打印session_id：{}'.format(session_id))


sleep(1)
logging.debug(msg='开始测试-打开测试网站')
# 打开测试网站
# /session/$sessionId/url
surl='http://127.0.0.1:9515/session/{}/url'.format(session_id)
data={'url':'http://120.78.128.25:8765/index/login.html'}
res=requests.post(surl,json=data)
# print(res.json())


sleep(1)
logging.debug(msg='='*10+'定位用户名输入框'+'='*10)
# 定位用户名输入框
# /session/$sessionId/element
surl_1='http://127.0.0.1:9515/session/{}/element'.format(session_id)
data={"using": "xpath", "value": "//input[@name='phone']"}
res_user=requests.post(surl_1,json=data)
logging.debug(msg='='*10+'定位用户名输入框接口地址是：{}、数据是：{}'.format(surl_1,data)+'='*10)
logging.debug(msg='='*10+'定位用户名输入框接口测试结果是是：{}'.format(res_user.status_code)+'='*10)
em=res_user.json()["value"]
us_id=get_value(em)
# print(us_id)


sleep(1)
logging.debug(msg='='*10+'输入用户名'+'='*10)
# 输入用户名
# /session/$sessionId/element/$id/value
# http://localhost:8888/session/{}/element/{}/value
surl_2='http://127.0.0.1:9515/session/{}/element/{}/value'.format(session_id, us_id)
# print(surl_2)
data_2={"text": "18684720553", "value": ["1", "8", "6", "8", "4", "7", "2", "0", "5", "5", "3"]}
res_2=requests.post(surl_2,json=data_2)
logging.debug(msg='='*10+'输入用户名输入框接口地址是：{}、数据是：{}'.format(surl_2,data_2)+'='*10)
logging.debug(msg='='*10+'输入用户名输入框接口测试结果是是：{}'.format(res_2.status_code)+'='*10)
# print(res_2.json())


sleep(1)
logging.debug(msg='='*10+'定位密码输入框'+'='*10)
# 定位密码输入框
# /session/$sessionId/element
surl_3='http://127.0.0.1:9515/session/{}/element'.format(session_id)
data_3={"using": "xpath", "value": "//input[@name='password']"}
res_pwd=requests.post(surl_3,json=data_3)
em=res_pwd.json()["value"]
ps_id=get_value(em)
logging.debug(msg='='*10+'定位用户名输入框接口地址是：{}、数据是：{}'.format(surl_3,data_3)+'='*10)
logging.debug(msg='='*10+'定位用户名输入框接口测试结果是是：{}'.format(res_pwd.status_code)+'='*10)


sleep(1)
logging.debug(msg='='*10+'输入密码'+'='*10)
# 输入密码
# /session/$sessionId/element/$id/value
surl_4='http://127.0.0.1:9515/session/{}/element/{}/value'.format(session_id, ps_id)
# print(surl_4)
data_4={"text": "python", "value": ["p", "y", "t", "h", "o", "n"]}
res_4=requests.post(surl_4,json=data_4)
logging.debug(msg='='*10+'输入用户名输入框接口地址是：{}、数据是：{}'.format(surl_4,data_4)+'='*10)
logging.debug(msg='='*10+'输入用户名输入框接口测试结果是是：{}'.format(res_4.status_code)+'='*10)
# print(res_2.json())


sleep(1)
logging.debug(msg='='*10+'定位登陆按钮'+'='*10)
# 点位按钮
# /session/$sessionId/element
surl_5='http://127.0.0.1:9515/session/{}/element'.format(session_id)
data_5={"using": "xpath", "value": "//button[contains(@class,'btn-special')]"}
res_bu=requests.post(surl_5,json=data_5)
bt=res_bu.json()["value"]
logging.debug(msg='='*10+'登陆按钮接口地址是：{}、数据是：{}'.format(surl_5,data_5)+'='*10)
logging.debug(msg='='*10+'登陆输入框接口测试结果是是：{}'.format(res_bu.status_code)+'='*10)
# bu_id=get_value(em)


sleep(1)
logging.debug(msg='='*10+'点击登陆按钮'+'='*10)
# 点击按钮
# /session/$sessionId/element/$id/click
url_6='http://127.0.0.1:9515/session/{}/element/{}/click'.format(session_id, get_value(bt))
# print(url_6)
data_6={"id": get_value(bt)}
res_6=requests.post(url_6,json=data_6)
logging.debug(msg='='*10+'点击按钮接口地址是：{}、数据是：{}'.format(url_6,data_6)+'='*10)
logging.debug(msg='='*10+'点击按钮接口测试结果是是：{}'.format(res_6.status_code)+'='*10)


sleep(1)
logging.debug(msg='='*10+'关闭浏览器'+'='*10)
# 关闭浏览器
# /session/$sessionId
url_7='http://127.0.0.1:9515/session/{}'.format(session_id)
requests.delete(url_7)
