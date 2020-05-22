# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver import Chrome

driver=Chrome()
cook={'domain': '120.78.128.25',
      'name': 'fengwoo',
      'path': '/',
      'value':'2shlsj8b6qju618hgj9ggjs2e3'}

driver.get('http://120.78.128.25:8765/Index/login.html')
driver.add_cookie(cook)
driver.get('http://120.78.128.25:8765')
# ele=driver.find_element_by_xpath("//a[text()='我的帐户[python10]']")
ele=driver.find_element_by_xpath("//a[contains(text(),'我的帐户')]")
ele2=driver.find_element_by_xpath("//a[contains(@href,'Member')]")
print(ele.text)
print(ele2.text)