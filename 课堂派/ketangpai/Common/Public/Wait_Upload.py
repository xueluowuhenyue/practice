# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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