# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.common.by import By
from random import choice
from time import sleep

driver=Chrome()
#打开网页
driver.get('https://www.ketangpai.com/')
#点击登录
wait=WebDriverWait(driver,10,0.3)
wait.until(e.presence_of_element_located((By.XPATH,"//a[text()='登录']"))).click()
sleep(3)
#截屏
driver.save_screenshot('login.png')
#填写登录信息
ele=WebDriverWait(driver,10).until(e.presence_of_element_located((By.NAME,'account')))
ele.send_keys('13541781424')
#填写密码
WebDriverWait(driver,5).until(e.presence_of_element_located((By.XPATH,"//input[@name='pass']"))).send_keys(19931025)
#点击登录
driver.find_element_by_xpath("//*[@name='account']/parent::div/../a[text()='登录']").click()
#进入班级
ele=WebDriverWait(driver,10,0.3).until(e.presence_of_element_located((By.XPATH,"//*[@class='ktdl1 ktpx1']//a[@class='jumptoclass']")))
ele.click()
#获取作业列表
wait=WebDriverWait(driver,10,0.3)
work_list=wait.until(e.presence_of_all_elements_located((By.XPATH,"//*[@class='homework-cont width980 editor-page']//a")))
#随机选择作业点击
ele=choice(work_list)
ele.click()
#截屏
sleep(3)
driver.save_screenshot('home_work.png')
#后退
driver.back()
#点击话题
wait=WebDriverWait(driver,10,0.3)
wait.until(e.presence_of_element_located((By.XPATH,"//a[text()='话题']"))).click()
# 获取当前url
print(driver.current_url)
#窗口最大化
driver.maximize_window()
#截屏
sleep(3)
driver.save_screenshot('topic.png')
#刷新
driver.refresh()
#点击资料
wait=WebDriverWait(driver,5,0.5)
wait.until(e.presence_of_element_located((By.XPATH,"//a[text()='资料']"))).click()
#截屏
sleep(3)
driver.save_screenshot('data.png')
#随机打开一个文件
file_list=WebDriverWait(driver,10).until(e.presence_of_all_elements_located((By.XPATH,"//*[@class='clearfix']/li")))
ele=choice(file_list)
ele.click()
#点击公告
wait=WebDriverWait(driver,10)
wait.until(e.presence_of_element_located((By.XPATH,"//a[text()='公告']"))).click()
#选择公告打开
msg_list=WebDriverWait(driver,10,0.3).until(e.presence_of_all_elements_located((By.XPATH,"//*[@id='viewer-annouce']//a")))
ele=choice(msg_list)
ele.click()
#截屏
sleep(3)
driver.save_screenshot('msg.png')
# #关闭浏览器
driver.close()