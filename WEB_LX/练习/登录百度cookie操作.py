# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver import Firefox

driver=Firefox()
# driver.get('https://www.baidu.com')
# # 点击登录
# driver.find_element_by_xpath("//div[@id='u1']//a[text()='登录']").click()
# sleep(1)
# driver.find_element_by_xpath("//p[text()='用户名登录']").click()
# sleep(2)
# # 输入用户名
# driver.find_element_by_xpath(
#     "//input[@name='userName']").send_keys('13541781424')
# # 输入密码
# driver.find_element_by_xpath("//input[@name='password']").send_keys('19931025')
# # 点击登录
# driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_10__submit']").click()
# cookie=driver.get_cookies()
# print(cookie)
cook={'domain': '.baidu.com',
      'name': 'BDUSS',
      'path': '/',
      'value': 'WhSMUpIOXhkOXBrZTF4TmRKMG1YYUkyb0JscGdNRE9kZH40WmpBaUZES35YVGhkSVFBQUFBJCQAAAAAAAAAAAEAAAD4pMmGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL~QEF2~0BBdQ'}

# 打开网页
driver.get('https://www.baidu.com')
# 添加cookit
driver.add_cookie(cook)
sleep(3)
# 进入网页
driver.get('http://i.baidu.com')