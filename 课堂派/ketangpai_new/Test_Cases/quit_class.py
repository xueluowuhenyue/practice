# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from Common.Public.do_excel import DoExcel
from Common.Public import project_path
from Common.Public.log_module import Mylog
from ddt import ddt,unpack,data
from Common.page.subclass import SubCalss
from Common.page.login import Login
from Common.Public.get_data import replace
import unittest
from time import sleep
logger=Mylog()


@ddt
class QuitClass(unittest.TestCase):
    l=DoExcel(project_path.excel_path).read_Excel('sub')

    def setUp(self):
        Login().driver.implicitly_wait(30)
        Login().register('13541781424','19931025')
    @data(*l)
    @unpack
    #老师为什么测试用例只能执行第一条?
    def test_quit_class(self,CaseId,Module,Title,Precondition,Steps,
                   Data,ExpectedResult,ActualResult,TestResult):
        Data=replace(Data)
        logger.info('正在执行{}条用例，测试数据是{}'.format(CaseId,Data))
        sleep(2)
        password=eval(Data)['password']
        SubCalss().sub_class('python14期考核',password)
        if CaseId==1:
            ele=Login().wait(By.XPATH,"//*[@id='show-tip']")
            msg=ele.text
            try:
                self.assertEqual(ExpectedResult,msg)
                TestResult='pass'
            except AssertionError as e:
                TestResult='failed'
                raise e
        else:
            ele=Login().wait(By.XPATH,"//*[@id='error-tip']")
            msg=ele.text
            try:
                self.assertEqual(ExpectedResult,msg)
                TestResult='pass'
            except AssertionError as e:
                TestResult='failed'
                raise e

        Login().driver.save_screenshot('D:\ketangpai\Data\img\sub_class.png')
        DoExcel(project_path.excel_path).write_Excel('sub',CaseId+1,8,msg)
        DoExcel(project_path.excel_path).write_Excel('sub',CaseId+1,9,TestResult)
        logger.info('测试结果是：{}'.format(TestResult))

    def tearDown(self):
        Login().driver.quit()

if __name__ == '__main__':
    QuitClass().test_quit_class()