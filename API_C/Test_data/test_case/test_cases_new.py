# -*- coding:utf-8 -*-
import unittest
import requests
from ddt import ddt,data,unpack
from API_C.Common.public.log_module import Mylog
from API_C.Common.public.read_excel import DoExcel
from API_C.Common.public import project_path
from API_C.Common.public.GETDATA import getdata
from API_C.Common.public.do_pymysql import Dopymysql
logger=Mylog()

@ddt
class testCases(unittest.TestCase):
    '''这是一个发送http请求的类'''
    t=DoExcel(project_path.excel_path).read_Excel('test')
    @data(*t)
    @unpack
    def test_cases(self,CaseId,Module,URL,Title,Method,Params,Sql,ExpectedResult,ActualResult,TestResult):
        '''这是一个用来测试注册登录的模块'''
        headers={'user-agent':'Mozilla/5.0','Connection':'keep-alive'}
        '''替换标ID'''
        if Sql!=None and Module=='recharge':
            '''获取充值前的金额'''
            MN=Dopymysql().select_db(eval(Sql)['sq2'],1)
            setattr(getdata,'MONEY',MN[0])

        if Sql!=None and Module=='withdraw':
            '''查询提现前的余额'''
            rm=Dopymysql().select_db(eval(Sql)['sq5'],1)
            setattr(getdata,'YUE',rm[0])

        if Sql!=None and Module=='bidLoan':
            '''查询竞标前的账户余额'''
            my=Dopymysql().select_db(eval(Sql)['sq3'],1)
            '''查询memberId'''
            fd=Dopymysql().select_db(eval(Sql)['sq4'],1)
            setattr(getdata,'MID',fd[0])

        # if Sql!=None and Module=='userlist':
        #     '''查询用户列表'''
        #     userno=Dopymysql().select_db(eval(Sql)['sq6'],2)

        if Params.find('mid') !=-1:
            '''替换memberId的值'''
            Params=Params.replace('mid',str(getattr(getdata,'MID')))

        if Params.find('num') !=-1:
            '''判断变量是否存在，替换标号'''
            Params=Params.replace('num',str(getattr(getdata,'NUM')))
        else:
            Params=Params
        logger.info('正在执行{}模块{}条用例，测试数据是{}'.format(Module,CaseId,Params))
        if Method=='post':                      #判断请求类型
            res=requests.post(URL,data=eval(Params),cookies=getattr(getdata,'cookies'))    #传参
        else:
            res=requests.get(URL,params=eval(Params),cookies=getattr(getdata,'cookies'))
        if res.cookies:
            '''判断cookies是否为空'''
            setattr(getdata,'cookies',res.cookies)         #更新cookies的值

        if Sql!=None and Module=='addLoan':
            '''判断查询语句是否存在'''
            '''查询标号'''
            data=Dopymysql().select_db(str(eval(Sql)['sql']),1)
            '''更新标号'''
            setattr(getdata,'NUM',data[0])

        if Sql!=None and Module=='bidLoan':
            '''查询竞标后的账户余额'''
            mk=Dopymysql().select_db(eval(Sql)['sq3'],1)
            try:
               int(mk[0])==int(my[0])-int(eval(Params)['amount'])    #竞标后的余额等于竞标前的余额减去投资金额
            except Exception as e:
                print('剩余金额不对')
                raise e

        if ExpectedResult.find('money') != -1:
            '''充值后的金额等于操作前的金额加充值金额，用money代替充值后的金额，int(eval(Params)['amount']为充值金额'''
            ExpectedResult=ExpectedResult.replace('money',str(int(eval(Params)['amount'])+getattr(getdata,'MONEY')))
        else:
            ExpectedResult=ExpectedResult

        if ExpectedResult.find('yue') != -1:
            '''提现后的金额等于提现前的金额减去提现值金额，用yue代替提现后的金额，int(eval(Params)['amount']为套现金额'''
            ExpectedResult=ExpectedResult.replace('yue',str(getattr(getdata,'YUE')-int(eval(Params)['amount'])))
        else:
            ExpectedResult=ExpectedResult
        DoExcel(project_path.excel_path).write_Excel('test',CaseId+1,9,res.text)
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
            DoExcel(project_path.excel_path).write_Excel('test',CaseId+1,10,TestResult)
            logger.info('实际结果是{}，测试结果是：{}'.format(res.text,TestResult))




