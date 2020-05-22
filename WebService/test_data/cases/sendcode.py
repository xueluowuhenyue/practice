# -*- coding:utf-8 -*-
import unittest
from suds.client import Client
from ddt import ddt,data,unpack
from WebService.Common.Public.do_pymysql import Dopymysql
from WebService.Common.Public.get_data import replace,judge_phone
from WebService.Common.Public.do_excel import DoExcel
from WebService.Common.Public.log_module import Mylog
from WebService.Common.Public import project_path
logger=Mylog()

@ddt
class SendCode(unittest.TestCase):
    l=DoExcel(project_path.excel_path).read_Excel('test')
    @data(*l)
    @unpack
    def test_sendCode(self,CaseId,Module,URL,Title,Params,SQL,ExpectedResult,ActualResult,TestResult):
        if  SQL !=None:
            SQL=replace(SQL)
        URL=replace(URL)            #替换url

        if SQL !=None:
            mn=Dopymysql().select_db(eval(SQL)['sql'])
        Params=replace(Params)

        logger.info('正在执行{}模块{}条用例，测试数据是{}'.format(Module,CaseId,Params))
        try:
            client=Client(URL)          #创建对象
            if Module=='sendmsg':
                res=client.service.sendMCode(eval(Params))           #获取返回数据
                if mn[0]==1:       #判断是否生成验证码
                    try:
                        '''判断期望和实际结果'''
                        self.assertEqual(eval(ExpectedResult)['retCode'],int(res.retCode))
                        self.assertEqual(eval(ExpectedResult)['retInfo'],res.retInfo)
                        TestResult='PASS'
                    except Exception as e:
                        TestResult='FAILED'
                        logger.error('出错啦错误是%s'%e)
                        raise e
                else:
                    TestResult='FAILED'
        except Exception as e:
            res=e
            self.assertEqual(ExpectedResult,str(res))
            TestResult='PASS'
        finally:
            '''写回测试结果'''
            DoExcel(project_path.excel_path).write_Excel('test',CaseId+1,8,str(res))
            DoExcel(project_path.excel_path).write_Excel('test',CaseId+1,9,TestResult)
            logger.info('实际结果是{}，测试结果是：{}'.format(res,TestResult))
