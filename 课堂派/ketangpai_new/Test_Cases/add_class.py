# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from Common.Public.do_excel import DoExcel
from Common.Public import project_path
from Common.Public.log_module import Mylog
from Common.page.addclass import AddCalss
from Common.page.login import Login
from Common.Public.get_data import replace
from ddt import ddt,data,unpack
from time import sleep
import unittest
logger=Mylog()

@ddt
class AddClass(unittest.TestCase,Login):
    #读取测试用例
    l=DoExcel(project_path.excel_path).read_Excel('add')
    @data(*l)
    @unpack
    def test_add_class(self, CaseId, Module, Title, Precondition, Steps,
                       Data, ExpectedResult, ActualResult, TestResult):

        Data=replace(Data)
        ExpectedResult=replace(ExpectedResult)
        logger.info('正在执行{}条用例，测试数据是{}'.format(CaseId,Data))
        #登录用户
        Login().register('13541781424', '19931025')
        #添加班级
        AddCalss().add_calss(data=eval(Data)['code'])
        sleep(2)
        self.driver.save_screenshot('D:\ketangpai\Data\img\\add_class.png')
        if CaseId == 1:
            #获取班级名称
            ele=Login().wait(By.XPATH,"//*[@id='viewer-container-lists']//*[@class='jumptoclass']")
            class_name=ele.get_attribute('title')
            try:
                self.assertEqual(ExpectedResult,class_name)
                TestResult = 'pass'
                # 进入课堂
                Login().wait(By.XPATH, "//a[@title='py14期考核']").click()
                sleep(2)
                Login().driver.save_screenshot('D:\ketangpai\Data\img\class.png')
                Login().driver.back()
            except AssertionError as e:
                TestResult = 'failed'
                raise e
        else:
            class_name=Login().wait(By.XPATH,"//*[@id='error-tip']").text
            try:
                self.assertEqual(ExpectedResult,class_name)
                TestResult = 'pass'
            except AssertionError as e:
                TestResult = 'failed'
                raise e

        '''写回测试结果'''
        DoExcel(project_path.excel_path).write_Excel('add',CaseId+1,8,class_name)
        DoExcel(project_path.excel_path).write_Excel('add',CaseId+1,9,TestResult)
        logger.info('测试结果是：{}'.format(TestResult))

    def tearDown(self):
        Login().driver.quit()


if __name__ == '__main__':
    unittest.main()