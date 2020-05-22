# -*- coding:utf-8 -*-
import unittest
import re
from suds.client import Client
from ddt import ddt,data,unpack
from WebService.Common.Public.do_pymysql import Dopymysql
from WebService.Common.Public.get_data import replace
from WebService.Common.Public.do_excel import DoExcel
from WebService.Common.Public.log_module import Mylog
from WebService.Common.Public import project_path
logger=Mylog()

@ddt
class TestCases(unittest.TestCase):
    l=DoExcel(project_path.excel_path).read_Excel('test')
    @data(*l)
    @unpack
    def test_01_sendMCode(self,CaseId,Module,URL,Title,Params,SQL,ExpectedResult,ActualResult,TestResult):
        if  SQL !=None:
            SQL=replace(SQL)
        URL=replace(URL)            #替换url
        # client=Client(URL)          #创建对象
        # if SQL !=None and Module=='sendmsg':
        #     mn=Dopymysql().select_db(eval(SQL)['sql'])

        if SQL !=None and Module=='register':
            '''查询验证码'''
            Fverify_code=Dopymysql().select_db(eval(SQL)['sq2'])
            # print(Fverify_code[0])
        if Params.find('fverifyCode') !=-1:
            '''替换验证码'''
            Params=Params.replace('fverifyCode',str(Fverify_code[0]))
        Params=replace(Params)

        logger.info('正在执行{}模块{}条用例，测试数据是{}'.format(Module,CaseId,Params))
        print(URL)
        try:
            client=Client(URL)          #创建对象
            if Module=='sendmsg':
                res=client.service.sendMCode(eval(Params))           #获取返回数据
                if SQL !=None and Module=='sendmsg':
                    mn=Dopymysql().select_db(eval(SQL)['sql'])
                    if mn[0]==1:       #判断验证码是否发送成功
                        pass
                    else:
                        logger.error('验证码发送失败')
                        TestResult='FAILED'
            else:
                res=client.service.userRegister(eval(Params))
            try:
                '''判断期望和实际结果'''
                self.assertEqual(eval(ExpectedResult)['retCode'],int(res.retCode))
                self.assertEqual(eval(ExpectedResult)['retInfo'],res.retInfo)
                TestResult='PASS'
            except Exception as e:
                TestResult='FAILED'
                logger.error('出错啦错误是%s'%e)
                raise e
        except Exception as e:
            res=e
            self.assertEqual(ExpectedResult,str(res))
            TestResult='PASS'
        finally:
            '''写回测试结果'''
            DoExcel(project_path.excel_path).write_Excel('test',CaseId+1,8,str(res))
            DoExcel(project_path.excel_path).write_Excel('test',CaseId+1,9,TestResult)
            logger.info('实际结果是{}，测试结果是：{}'.format(res,TestResult))

