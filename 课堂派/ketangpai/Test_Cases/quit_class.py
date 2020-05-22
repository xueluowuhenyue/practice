# -*- coding:utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Common.Public.do_excel import DoExcel
from Common.Public import project_path
from Common.Public.log_module import Mylog
from ddt import ddt,unpack,data
from Common.Public.login import Login
from Common.Public.get_data import replace
import unittest
from time import sleep
logger=Mylog()

@ddt
class QuitClass(unittest.TestCase):
    l=DoExcel(project_path.excel_path).read_Excel('web')

    def setUp(self):
        Login().driver.implicitly_wait(30)
        Login().register()
    @data(*l)
    @unpack
    def test_quit_class(self,CaseId,Module,Title,Precondition,Steps,
                   Data,ExpectedResult,ActualResult,TestResult):
        Data=replace(Data)
        if Module=='quit':
            logger.info('正在执行{}条用例，测试数据是{}'.format(CaseId,Data))
            #定位三个点
            Login().wait(By.XPATH,"//*[@data-id='MDAwMDAwMDAwMLOsuZmIqcmw']//a[@class='kdmore']").click()
            #点击退课
            # Login().wait(By.XPATH,"//*[@data-id='MDAwMDAwMDAwMLOsuZmHz9Fo']//a[text()='退课']").click()
            ac=ActionChains(Login().driver)
            ele=Login().wait(By.XPATH,"//*[text()='退课']")
            ac.move_to_element(ele).click(ele).perform()
            #输入密码
            Login().wait(By.XPATH,"//*[@class='deletekccon']//input").send_keys('19931025')
            #点击退课
            Login().wait(By.XPATH,"//*[@class='deletekt']//*[text()='退课']").click()
            sleep(2)
            Login().driver.save_screenshot('D:\ketangpai\Data\img\sub_class.png')

            ele=Login().wait(By.XPATH,"//*[@id='viewer-container-lists']//*[@class='jumptoclass']")
            end_name=ele.get_attribute('title')
            try:
                self.assertNotEqual(ExpectedResult,end_name)
                TestResult='pass'
            except AssertionError as e:
                TestResult='failed'
                raise e
            finally:
                '''写回测试结果'''
                DoExcel(project_path.excel_path).write_Excel('web',CaseId+1,8,end_name)
                DoExcel(project_path.excel_path).write_Excel('web',CaseId+1,9,TestResult)
                logger.info('测试结果是：{}'.format(TestResult))

    def tearDown(self):
        Login().driver.quit()