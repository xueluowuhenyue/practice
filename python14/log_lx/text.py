# -*- coding:utf-8 -*-
import unittest
from python14.log_lx.read_excel import DoExcel
p=DoExcel('D:\pycharm\python14\log_lx\py14.xlsx','test')
suite=unittest.TestSuite()
suite.addTest(DoExcel('creat_Excel'))
suite.addTest(DoExcel('write_Excel'))
suite.addTest(DoExcel('read_Excel'))
# loader=unittest.TestLoader
# suite.addTest(loader.loadTestsFromTestCase(DoExcel))

with open('test.txt','w',encoding='utf-8') as file:
    runner=unittest.TextTestRunner(stream=file,verbosity=2)
    runner.run(suite)#执行测试套件里面的用例