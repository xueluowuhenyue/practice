import unittest
import HTMLTestRunnerNew
from unittest框架 import test_case


suite=unittest.TestSuite()
# suite.addTest(TestAdd('test_001_two_positive'))
# suite.addTest(TestSub('test_005_two_negative'))

loader=unittest.TestLoader()
# 按类名导入用例
# suite.addTest(loader.loadTestsFromTestCase(test_case.TestAdd))
# suite.addTest(loader.loadTestsFromTestCase(test_case.TestSub))
# 按模块导入用例
suite.addTest(loader.loadTestsFromModule(test_case))

with open('test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='单元测试框架',
                                            description='20191202测试',
                                            tester='xiaoming')
    runner.run(suite)
# with open('test.txt','w+',encoding='utf-8') as file:
#     runner=unittest.TextTestRunner(stream = file,
#                                    verbosity =2)
#     runner.run(suite)