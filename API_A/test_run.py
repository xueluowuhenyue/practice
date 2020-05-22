# -*- coding:utf-8 -*-
import HTMLTestRunnerNew
import unittest
from API_A.Test_data.test_case import test_cases
from API_A.Common.public import project_path
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_cases))

with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='接口测试',
                                           description='登录模块测试',
                                           tester='小明')
    runner.run(suite)
