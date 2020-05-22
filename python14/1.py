# -*- coding:utf-8 -*-

from suds.client import Client

# url='http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
url='http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'

client=Client(url)
# d={'client_ip':'192.168.1.107','tmpl_id':1,'mobile':''}
d={'verify_code':'865562','user_id':'18296207777','channel_id':3,'pwd':'123456','mobile':'182962089167','ip':'192.168.1.107'}
# t1=update_time('2019-04-24 23:01:05')
# nowTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
# t2=update_time(nowTime)
# if t2-t1<=900:
#     print('未过期')
# else:
#     print('已过期')
try:
    # result=client.service.sendMCode(d)
    result=client.service.userRegister(d)
    # print(type(result.retCode))
    print(result)
except Exception as e:
    print(e)
    # p="Server raised fault: '手机号码错误'"
    # m=re.search(p,str(e)).group()
    # print(m)



# driver=webdriver.Firefox()
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('cbv')
# driver.find_element_by_xpath("//*[text()='贴吧']/parent::div/preceding-sibling::div//*[text()='百度首页']").click()
# driver.close()

# nowTime_str = datetime.datetime.now().strftime('%Y-%m-%d')
# # print(nowTime_str)
# #mktime参数为struc_time,将日期转化为秒，
# e_time = time.mktime(time.strptime(nowTime_str,"%Y-%m-%d"))
# print(e_time)
