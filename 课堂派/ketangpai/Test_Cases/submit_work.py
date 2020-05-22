# -*- coding:utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Common.Public.do_excel import DoExcel
from Common.Public import project_path
from Common.Public.log_module import Mylog
from ddt import ddt,unpack,data
from Common.Public.login import Login
from time import sleep
import unittest
logger=Mylog()

# @ddt
# class uploadWork(unittest.TestCase,Login):
#     #读取测试用例
#     l=DoExcel(project_path.excel_path).read_Excel('web')

    # def setUp(self):
Login().register()
#
# @data(*l)
# @unpack
# def test_upload(self,CaseId,Module,Title,Precondition,Steps,
#                Data,ExpectedResult,ActualResult,TestResult):

# logger.info('正在执行{}条用例，测试数据是{}'.format(CaseId,Data))
#进入班级
Login().wait(By.XPATH,"//a[@title='python全栈第14期' and @class='jumptoclass']").click()
#进入项目实战作业
# Login().wait(By.XPATH,"//a[@title='项目实战作业']").click()
#
# #定位作业列表
# ele=Login().wait(By.XPATH,"//*[@class='work-list']//h3")
# context=ele.text
# if context=="即将提交的文件":
    # 点击上传文件
    # ac=ActionChains(Login().driver)
    # ele=Login().wait(By.XPATH,"//*[text()='上传文件']")
    # ac.move_to_element(ele).click().perform()
    # sleep(2)
    # Login().upload_file('D:\\ketangpai\\Test_Cases\\quit_class.py')
    # sleep(2)
    # Login().wait(By.XPATH,"//a[contains(@class,'new-tj2')]").click()
# else:
#     #定位更新提交按钮
#     ele=Login().wait(By.XPATH,"//a[text()='更新提交' and @class='new-tj1']")
#     #创建一个新的动作链。
#     ac=ActionChains(Login().driver)
#     #将鼠标移动到更新提交按钮上点击按钮
#     ac.move_to_element(ele).click().perform()
#     #定位弹窗
#     Login().wait(By.XPATH,"//*[@id='update-pop']//a[text()='确定']").click()
#     #定位上传文件
#     ele=Login().wait(By.XPATH,"//*[text()='上传文件']")
#     #将鼠标移动到上传文件按钮上
#     ac.move_to_element(ele).perform()
#     #点击按钮
#     ac.click().perform()
#     sleep(2)
#     #上传文件
#     Login().upload_file("C:\\Users\\沈勇军\\Desktop\\file_upload.py")
#     #点击提交
#     sleep(2)
#     Login().wait(By.XPATH,"//a[contains(@class,'new-tj2')]").click()
#     e=wait(By.XPATH,"//a[contains(@class,'new-tj2')]")
#     #将鼠标移动到上传文件按钮上
#     ac.move_to_element(e).click().perform()

#点击作业留言
# Login().wait(By.XPATH,"//*[contains(@class,'work-message clearfix')]/*[@class='s2']").click()
# Login().wait(By.XPATH,"//*[@id='comment']").send_keys('哈哈哈')
# #点击保存
# Login().wait(By.XPATH,"//a[text()='保存']").click()
# sleep(2)
# Login.driver.save_screenshot('msg.png')
# 点击提交
# Login().wait(By.XPATH,"//*[text()='提交']").click()
# Login.driver.back()
#查看作业提交状态
ele=Login().wait(By.XPATH,"//a[@title='项目实战作业']/parent::h3/parent::div/parent::div//a[@class='sc-btn']")
context=ele.text
print(context)
# sleep(2)
# # Login.driver.save_screenshot('status.png')