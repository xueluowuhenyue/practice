# -*- coding:utf-8 -*-
import pytest
from time import sleep
from data.testdata import bid_data
from Common.Public.Log import Mylog

logger=Mylog()


@pytest.mark.parametrize('data', bid_data.error_bid)
def test_error_bid(data, init_bid):
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},投资金额是:{},期望结果是:{}'.format(data['module'],
                    data['Caseid'], data['title'], data['amount'], data['expect']))
    bid=init_bid[2]
    # 进入投资界面
    bid.the_tender(data['amount'])
    # 获取弹窗提示
    msg = bid.get_toast_text(data['text'])
    print(msg)
    try:
        assert (msg == data['expect'])
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


@pytest.mark.parametrize('data', bid_data.success_bid)
def test_success_bid(data, init_bid):
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},投资金额是:{},期望结果是:{}'.format(data['module'],
                data['Caseid'], data['title'], data['amount'], data['expect']))
    bid=init_bid[2]
    # 进入投资界面
    amount = bid.the_tender(data['amount'])
    # 获取弹窗提示
    msg = bid.get_msg()
    # 点击确定
    bid.click_determine()
    # 点击返回
    bid.click_back()
    sleep(1)
    # 点击“我”
    bid.click_user()
    # 获取投资后的余额
    end_money=bid.get_leave_amount()
    try:
        assert (msg == data['expect'])
        # 判断投资后的金额是否正确
        assert (amount-end_money == int(data['amount']))
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


if __name__ == '__main__':
    pytest.main()
