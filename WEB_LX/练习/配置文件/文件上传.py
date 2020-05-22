# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome, ActionChains
from time import time,sleep
import win32gui
import win32con

driver=()

driver.get('https://www.ketangpai.com')

driver.find_element_by_xpath("//*[@class='login']").click()
input_list=driver.find_elements_by_xpath("//*[@class='padding-cont pt-login']//input")
for i in input_list:
    if i.get_attribute('type')=='text':
        i.send_keys('13541781424')
    else:
        i.send_keys('19931025')

driver.find_element_by_xpath("//*[@class='padding-cont pt-login']//*[text()='登录']").click()
sleep(3)
driver.find_element_by_xpath("//a[@class='jumptoclass']").click()
sleep(3)
driver.find_element_by_xpath("//*[text()='交互操作作业']").click()
sleep(5)

ele=driver.find_element_by_xpath("//*[text()='上传文件']")

ac=ActionChains(driver)
ac.move_to_element(ele).perform()
ac.click().perform()
#一级窗口
dialog = win32gui.FindWindow("#32770","打开")
#二级
comboBoxEx32=win32gui.FindWindowEx(dialog,0,"comboBoxEx32",None)

comboBox=win32gui.FindWindowEx(comboBoxEx32,0,"comboBox",None)

edit=win32gui.FindWindowEx(comboBox,0,"edit",None)
button=win32gui.FindWindowEx(dialog,0,'Button',None)

win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,"C:\\Users\Administrator\gundongtiao.py")
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)

sleep(10)
driver.find_element_by_xpath("//a[text()='提交']").click()

sleep(5)