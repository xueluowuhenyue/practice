# -*- coding:utf-8 -*-
import HTMLTestRunnerNew
import unittest
from Test_Cases import Add_Class
from Test_Cases import Quit_Class
from Common.Public import project_path
import sys
# sys.path.append('./')

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(Add_Class))
suite.addTest(loader.loadTestsFromModule(Quit_Class))

with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='接口测试',
                                           description='web测试',
                                           tester='小明')
    runner.run(suite)