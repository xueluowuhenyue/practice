# -*- coding:utf-8 -*-
import unittest
import requests
from ddt import ddt,data,unpack
from API_D.Common.public.log_module import Mylog
from API_D.Common.public.read_excel import DoExcel
from API_D.Common.public import project_path
logger=Mylog()
cookies=None    #cookies为全局变量
@ddt
class testCases(unittest.TestCase):
    '''这是一个发送http请求的类'''
    t=DoExcel(project_path.excel_path).read_Excel('test')
    @data(*t)
    @unpack
    def test_cases(self,CaseId,Module,URL,Title,Method,Params,ExpectedResult,ActualResult,TestResult):
        '''这是一个用来测试注册登录的模块'''
        headers={'user-agent':'Mozilla/5.0','Connection':'keep-alive'}
        logger.info('正在执行{}模块{}条用例，测试数据是{}'.format(Module,CaseId,Params))
        global cookies                         #申明全局变量
        if Method=='post':                      #判断请求类型
            res=requests.post(URL,data=eval(Params),cookies=cookies)
        else:
            res=requests.get(URL,params=eval(Params),cookies=cookies)
        if res.cookies:
            '''判断cookies是否为空'''
            cookies=res.cookies
        DoExcel(project_path.excel_path).write_Excel('test',CaseId+1,8,res.text)
        '''将实际结果写入表格中'''
        try:
            '''判断期望和实际结果'''
            self.assertEqual(eval(ExpectedResult),res.json())
            TestResult='PASS'
        except Exception as e:
            TestResult='FAILED'
            logger.error('出错啦错误是%s'%e)
            raise e
        finally:
            '''写回测试结果'''
            DoExcel(project_path.excel_path).write_Excel('test',CaseId+1,9,TestResult)
            logger.info('实际结果是{}，测试结果是：{}'.format(res.text,TestResult))




