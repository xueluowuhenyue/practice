from time import sleep

from selenium.webdriver import Chrome
import logging

logging.basicConfig(level=logging.DEBUG)
print("="*5+'初始化浏览器'+"="*5)
driver=Chrome()


sleep(3)
print("="*5+'输入网址'+"="*5)
driver.get('http://120.78.128.25:8765/index/login.html')

sleep(3)
print("="*5+'定位用户名输入框'+"="*5)
ele=driver.find_element_by_xpath("//input[@name='phone']")

sleep(1)
print("="*5+'输入用户名'+"="*5)
ele.send_keys('18684720553')

print("="*5+'定位密码输入框'+"="*5)
ele=driver.find_element_by_xpath("//input[@name='password']")

sleep(1)
print("="*5+'输入密码'+"="*5)
ele.send_keys('python')

sleep(1)
print("="*5+'定位按钮'+"="*5)
ele=driver.find_element_by_xpath("//button[text()='登录']")

sleep(5)
print("="*5+'点击按钮'+"*****"+"="*5)
ele.click()