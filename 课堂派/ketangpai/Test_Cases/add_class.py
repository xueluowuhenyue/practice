# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from Common.Public.do_excel import DoExcel
from Common.Public import project_path
from Common.Public.log_module import Mylog
from ddt import ddt,unpack,data
from Common.Public.login import Login
from Common.Public.get_data import replace
from selenium.webdriver import Chrome
from time import sleep
import unittest
logger=Mylog()


@ddt
class AddClass(unittest.TestCase,Login):
    #读取测试用例
    l=DoExcel(project_path.excel_path).read_Excel('web')

    def setUp(self):
        Login().driver.implicitly_wait(30)
        Login().register()
    @data(*l)
    @unpack
    def test_add_class(self,CaseId,Module,Title,Precondition,Steps,
                   Data,ExpectedResult,ActualResult,TestResult):
        Data=replace(Data)
        ExpectedResult=replace(ExpectedResult)
        logger.info('正在执行{}条用例，测试数据是{}'.format(CaseId,Data))
        #点击加入班级
        Login().wait(By.XPATH,"//*[text()='加入班级' and contains(@class,'ktcon1l')]").click()
        #定位输入框
        ele=Login().wait(By.XPATH,"//*[@class='chuangjiankccon']/input")
        #输入验证码
        ele.send_keys(eval(Data)['code'])
        #点击加入按钮
        Login().wait(By.XPATH,"//*[@class='cjli2']/a").click()
        sleep(2)
        self.driver.save_screenshot('D:\ketangpai\Data\img\\add_class.png')
        #获取班级名称
        ele=Login().wait(By.XPATH,"//*[@id='viewer-container-lists']//*[@class='jumptoclass']")
        class_name=ele.get_attribute('title')
        try:
            self.assertEqual(ExpectedResult,class_name)
            TestResult = 'pass'
        except AssertionError as e:
            TestResult = 'failed'
            raise e
        finally:
            '''写回测试结果'''
            DoExcel(project_path.excel_path).write_Excel('web',CaseId+1,8,class_name)
            DoExcel(project_path.excel_path).write_Excel('web',CaseId+1,9,TestResult)
            # 进入课堂
            Login().wait(By.XPATH,"//a[@title='py14期考核']").click()
            sleep(2)
            Login().driver.save_screenshot('D:\ketangpai\Data\img\class.png')
            Login().driver.back()

    def tearDown(self):
        Login().driver.quit()