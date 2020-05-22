# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import win32gui
import win32con

class Login:
    driver=Chrome()
    # 打开网页
    driver.get("https://www.ketangpai.com")

    def wait(self,method,ele,num=1) ->WebElement:
        '''本函数用于等待'''
        Wait=WebDriverWait(self.driver,10)
        if num==1:
            e=Wait.until(ec.presence_of_element_located((method,ele)))
        else:
            e=Wait.until(ec.presence_of_all_elements_located((method,ele)))
        return e

    def register(self,username,password):
        '''登录函数，username为用户名；password为密码'''
        #点击登录
        # self.driver.find_element_by_xpath("//*[@class='login']").click()
        # WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//*[@class='login']")))
        self.wait(By.XPATH,"//*[@class='login']").click()
        #定位输入框
        input_list=self.wait(By.XPATH,"//*[@class='padding-cont pt-login']//input",2)
        for i in input_list:
            if i.get_attribute('type')=='text':
                '''定位用户名输入框'''
                i.send_keys(username)
            else:
                '''定位用户名输入框'''
                i.send_keys(password)
        #点击登录按钮
        self.wait(By.XPATH,"//*[@class='padding-cont pt-login']//*[text()='登录']").click()

    def upload_file(self,file_path):
     '''本函数用于文件上传'''
     #定位一级窗口
     dialog = win32gui.FindWindow("#32770","打开")
     #定位二级窗口
     comboBoxEx32=win32gui.FindWindowEx(dialog,0,"comboBoxEx32",None)
     #定位三级窗口
     comboBox=win32gui.FindWindowEx(comboBoxEx32,0,"comboBox",None)
     #定位四级窗口
     edit=win32gui.FindWindowEx(comboBox,0,"edit",None)
     button=win32gui.FindWindowEx(dialog,0,'Button',None)
     #文件上传
     win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)
     win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)

if __name__ == '__main__':
    Login().register('13541781424','19931025')