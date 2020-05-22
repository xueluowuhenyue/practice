# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import time,sleep
import win32gui
import win32con


driver=Chrome()


def wait(method,ele,num=1) ->WebElement:
    '''本函数用于等待'''
    Wait=WebDriverWait(driver,10)
    if num==1:
        e=Wait.until(ec.presence_of_element_located((method,ele)))
    else:
        e=Wait.until(ec.presence_of_all_elements_located((method,ele)))
    return e


def upload_file(file_path):
    '''本函数用于文件上传'''
    # 定位一级窗口
    dialog = win32gui.FindWindow("#32770","打开")
    # 定位二级窗口
    comboBoxEx32=win32gui.FindWindowEx(dialog,0,"comboBoxEx32",None)
    # 定位三级窗口
    comboBox=win32gui.FindWindowEx(comboBoxEx32,0,"comboBox",None)
    # 定位四级窗口
    edit=win32gui.FindWindowEx(comboBox,0,"edit",None)
    button=win32gui.FindWindowEx(dialog,0,'Button',None)
    # 文件上传
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)

# 打开课堂派
driver.get('https://www.ketangpai.com')
# 点击登录
wait(By.XPATH,"//*[@class='login']").click()
# 定位输入框
input_list=wait(By.XPATH,"//*[@class='padding-cont pt-login']//input",2)
for i in input_list:
    if i.get_attribute('type')=='text':
        '''定位用户名输入框'''
        i.send_keys('13541781424')
    else:
        '''定位用户名输入框'''
        i.send_keys('19931025')

# 点击登录按钮
wait(By.XPATH,"//*[@class='padding-cont pt-login']//*[text()='登录']").click()
# 点击python全栈第14期
wait(By.XPATH,"//a[@class='jumptoclass']").click()
sleep(3)
# 选择点击交互操作作业
wait(By.XPATH,"//*[text()='交互操作作业']").click()

# 定位更新提交按钮
ele=wait(By.XPATH,"//a[text()='更新提交' and @class='new-tj1']")
# 创建一个新的动作链。
ac=ActionChains(driver)
# 将鼠标移动到更新提交按钮上
ac.move_to_element(ele).perform()
ac.drag_and_drop()
# 点击按钮
ac.click().perform()
sleep(5)
# 定位弹窗
# alter=driver.switch_to.alert
# #点击确定
# alter.accept()
wait(By.XPATH,"//*[@id='update-pop']//a[text()='确定']").click()
# 定位上传文件
ele=wait(By.XPATH,"//*[text()='上传文件']")
# 将鼠标移动到上传文件按钮上
ac.move_to_element(ele).perform()
# 点击按钮
ac.click().perform()
sleep(2)
# 上传文件
upload_file("C:\\Users\\沈勇军\\Desktop\\file_upload.py")
# 点击提交
sleep(2)
wait(By.XPATH,"//a[contains(@class,'new-tj2')]").click()
# e=wait(By.XPATH,"//a[contains(@class,'new-tj2')]")
# #将鼠标移动到上传文件按钮上
# ac.move_to_element(e).perform()
# #点击按钮
# ac.click().perform()
sleep(2)
driver.quit()

