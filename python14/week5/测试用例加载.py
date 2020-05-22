# -*- coding:utf-8 -*-
import unittest
#suite:集合套件  testsuite测试套件 存储加载用例
suite=unittest.testsuite()#创建对象

#方法一  加载用例suite.addTest
#suite.addtest('测试类'('用例'))  #只能增加测试类的实例/对象

#方法二  通过类进行加载
# loader=unittest.TestLoader()    #加载用例
# suite.addTest(loader.loadTestsFromTestCase('测试类名'))     #直接传测试类名

#方法三 通过模块加载用例
# suite.addTest(loader.loaderTestsFromModule('模块名'))