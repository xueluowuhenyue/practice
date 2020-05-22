# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from Common.Public.do_excel import DoExcel
from Common.Public import project_path
from Common.Public.log_module import Mylog
from ddt import ddt,unpack,data
from Common.Public.login import Login
from Common.Public.get_data import replace
from time import sleep
import unittest
logger=Mylog()


@ddt
class AddClass(unittest.TestCase,Login):
    #读取测试用例
    l=DoExcel(project_path.excel_path).read_Excel('web')

    def setUp(self):
        Login().register('13541781424','19931025')

    @data(*l)
    @unpack
    def test_add_class(self,CaseId,Module,Title,Precondition,Steps,
                   Data,ExpectedResult,ActualResult,TestResult):
        Data=replace(Data)
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
        ele=Login().wait(By.XPATH,"//*[@data-id='MDAwMDAwMDAwMLOsuZmHz9Fo']//*[@class='jumptoclass']")
        class_name=ele.get_attribute('title')
        try:
            self.assertEqual(ExpectedResult,class_name)
        except AssertionError as e:
            raise e
        finally:
            '''写回测试结果'''
            DoExcel(project_path.excel_path).write_Excel('web',CaseId+1,8,class_name)
            DoExcel(project_path.excel_path).write_Excel('web',CaseId+1,9,TestResult)

        #进入课堂
        Login().wait(By.XPATH,"//a[@title='python14期考核']").click()
        sleep(2)
        self.driver.save_screenshot('D:\ketangpai\Data\img\class.png')
        self.driver.back()
        #定位三个点
        Login().wait(By.XPATH,"//*[@data-id='MDAwMDAwMDAwMLOsuZmHz9Fo']//a[@class='kdmore']").click()
        #点击退课
        Login().wait(By.XPATH,"//*[@data-id='MDAwMDAwMDAwMLOsuZmHz9Fo']//a[text()='退课']").click()
        #输入密码
        Login().wait(By.XPATH,"//*[@class='deletekccon']//input").send_keys('19931025')
        #点击退课
        Login().wait(By.XPATH,"//*[@class='deletekt']//*[text()='退课']").click()
        sleep(2)
        self.driver.save_screenshot('D:\ketangpai\Data\img\sub_class.png')

        ele=Login().wait(By.XPATH,"//*[@data-id='MDAwMDAwMDAwMLOcz5mGqclt']//*[@class='jumptoclass']")
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
        self.driver.quit()