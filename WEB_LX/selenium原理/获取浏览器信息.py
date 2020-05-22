# encoding:utf8
from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)
dr = webdriver.Chrome()
dr.implicitly_wait(10)
# 打开深圳-逸遥 博客园首页
dr.get('https://www.cnblogs.com/snailrunning')
# 定位深圳-逸遥 第一篇博文标题
el = dr.find_element_by_css_selector('.postTitle a')
# 点击第一篇博文标题
el.click()