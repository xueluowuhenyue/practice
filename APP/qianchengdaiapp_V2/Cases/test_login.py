# -*- coding:utf-8 -*-
import pytest
from data.testdata import login_data
from time import sleep
from Common.Public.Log import Mylog
logger=Mylog()


@pytest.mark.parametrize('data', login_data.mobile_error)
def test_mobile_error(data, init_app):
    ' ''手机号码错误'' '
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},期望结果是:{}'.format(data['module'],
               data['Caseid'], data['title'],data['mobile'], data['expect']))
    login=init_app[1]
    # 登录用户
    login.login(data['mobile'])
    # 获取弹窗提示
    text = login.get_toast_text(data['text'])
    try:
        assert (text == data['expect'])
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        '''点击确定按钮'''
        login.popup_prompt()
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


@pytest.mark.parametrize('data', login_data.no_register)
def test_no_register(data, init_app):
    ' ''手机号码错误'' '
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},期望结果是:{}'.format(data['module'],
               data['Caseid'], data['title'],data['mobile'], data['expect']))
    login=init_app[1]
    driver = init_app[0]
    # 登录用户
    login.login(data['mobile'])
    # 获取弹窗提示
    text = login.get_toast_text(data['text'])
    activity = driver.current_activity
    try:
        assert (text == data['expect'])
        # 判断是否跳转到注册页面
        assert (activity == '.activity.addition.RegisterActivity')
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        '''点击确定按钮'''
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


@pytest.mark.parametrize('data', login_data.pwd_error)
def test_password_error(data, init_app):
    ' ''密码错误'' '
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},登录密码是:{},期望值是:{}'.format(data['module'],
               data['Caseid'], data['title'],data['mobile'], data['pwd'], data['expect']))
    login = init_app[1]
    # 登录用户
    login.login(data['mobile'])
    sleep(1)
    login.clear_password()
    # 输入登录密码
    login.get_password_input().send_keys(data['pwd'])
    # 点击确定
    login.click_next()
    # 获取页面
    # page=driver.current_activity
    # 获取弹窗提示
    text = login.get_toast_text('错误')
    try:
        assert (text == data['expect'])
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


@pytest.mark.parametrize('data', login_data.login_success)
def test_success(data, init_app):
    ' ''正确登录'' '
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},登录密码是:{},期望值是:{}'.format(data['module'],
               data['Caseid'], data['title'],data['mobile'], data['pwd'], data['expect']))
    login = init_app[1]
    caps = init_app[2]
    # 登录用户
    login.login(data['mobile'])
    sleep(1)
    login.get_password_input().send_keys(data['pwd'])
    # 点击确定
    login.click_next()
    sleep(2)
    if caps['noReset'] ==  False:
        # 点击“以后再说”
        login.click_talk_later()
        sleep(1)
    else:
        login.click_me()
    # 获取用户名
    username=login.get_username()
    try:
        assert (username == data['expect'])
        Testresult = 'PASS'
    except AssertionError as e:
        Testresult = 'FAIL'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


if __name__ == '__main__':
    # pytest.main(['-v', '-n', 'auto'])
    pytest.main()