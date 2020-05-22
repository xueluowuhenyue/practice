# -*- coding:utf-8 -*-
from time import sleep
import pytest
import yaml
from appium.webdriver import Remote
from Pages.loginpage import Login
from Pages.homepage import Home
from Pages.bidpage import Bid
from Common.Public import project_path

caps=yaml.load(open(project_path.device_info_path, encoding='utf-8'),
               Loader=yaml.FullLoader)


@pytest.fixture(scope="function", params=['Reset', 'noReset'])
def init_app(request):
    ' ''初始化APP'' '
    if request.param == 'Reset':
        # 重置APP
        caps['noReset'] = False
        driver = Remote(desired_capabilities=caps)
        login = Login(driver)
        home = Home(driver)
        sleep(3)
        # 进入首页
        home.homepage()
        sleep(1)
    else:
        # 不重置APP
        caps['noReset'] = True
        driver = Remote(desired_capabilities=caps)
        # 初始化登录页面
        login = Login(driver)
        sleep(3)
    # 点击注册/登录
    login.click_login()
    yield driver, login, caps
    driver.quit()


# def init_app_reset():
#     # 重置APP
#     caps['noReset'] = False
#     driver = Remote(desired_capabilities=caps)
#     login = Login(driver)
#     home = Home(driver)
#     sleep(3)
#     # 进入首页
#     home.homepage()
#     sleep(1)
#     return driver,login
#
#
@pytest.fixture(scope="function")
def init_bid():
    ' ''不重置APP'' '
    caps['noReset'] = False
    driver = Remote(desired_capabilities=caps)
    # 初始化登录页面
    login = Login(driver)
    home = Home(driver)
    bid = Bid(driver)
    sleep(3)
    # 进入首页
    home.homepage()
    # 点击注册/登录
    login.click_login()
    # 输入用户名
    login.login()
    # 输入密码
    login.get_password_input().send_keys('python')
    # 点击下一步
    login.click_next()
    login.click_talk_later()
    yield driver, login, bid
    driver.quit()


if __name__ == '__main__':
    pass
