# -*- coding:utf-8 -*-
import unittest
from suds.client import Client
from ddt import ddt,data,unpack
from WebService.Common.Public.do_pymysql import Dopymysql
from WebService.Common.Public.get_data import replace,judge_phone
from WebService.Common.Public.do_excel import DoExcel
from WebService.Common.Public.log_module import Mylog
from WebService.Common.Public import project_path
import datetime
import time
logger=Mylog()

Fverify_code=''
@ddt
class Register(unittest.TestCase):
    l=DoExcel(project_path.excel_path).read_Excel('test')
    @data(*l)
    @unpack
    def test_register(self,CaseId,Module,URL,Title,Params,SQL,ExpectedResult,ActualResult,TestResult):
        if  SQL !=None:
            SQL=replace(SQL)
        URL=replace(URL)            #替换url

        if  CaseId==5:
            '''查询验证码'''
            global Fverify_code
            Fverify_code=Dopymysql().select_db(eval(SQL)['sq2'])

        if Params.find('fverifyCode') !=-1:
            '''替换验证码'''
            Params=Params.replace('fverifyCode',str(Fverify_code[0]))

        Params=replace(Params)
        logger.info('正在执行{}模块{}条用例，测试数据是{}'.format(Module,CaseId,Params))
        try:
            client=Client(URL)          #创建对象
            res=client.service.userRegister(eval(Params))
            if CaseId ==5:
                us=Dopymysql().select_db(eval(SQL)['sq3'])
                num=Dopymysql().select_db(eval(SQL)['sq4'])
                if us[0] !=eval(Params)['pwd'] and us[0] !=eval(Params)['user_id'] and num[0]==1:
                    '''查询信息是否加密，并且生成一条注册信息'''
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
            else:
                try:
                    '''判断期望和实际结果'''
                    self.assertNotEqual(eval(ExpectedResult)['retCode'],int(res.retCode))
                    self.assertNotEqual(eval(ExpectedResult)['retInfo'],res.retInfo)
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

