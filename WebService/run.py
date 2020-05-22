# -*- coding:utf-8 -*-
import HTMLTestRunnerNew
import unittest
from WebService.test_data.cases import sendcode
from WebService.test_data.cases import register
from WebService.Common.Public import project_path
import sys
# sys.path.append('./')

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(sendcode))
suite.addTest(loader.loadTestsFromModule(register))
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='接口测试',
                                           description='webservice接口测试',
                                           tester='小明')
    runner.run(suite)