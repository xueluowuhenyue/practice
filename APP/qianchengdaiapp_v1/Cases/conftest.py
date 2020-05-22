# -*- coding:utf-8 -*-
import pytest
from data import devices_info
from appium.webdriver import Remote
from Pages.login import Login
from Pages.home import Home
from Pages.pwd import Pwd


@pytest.fixture(scope="module")
def init_pwd():
    driver = Remote(desired_capabilities=devices_info.caps)
    driver.implicitly_wait(30)
    # 初始化登录页面
    login = Login(driver)
    home = Home(driver)
    pwd= Pwd(driver)
    yield driver,login,home,pwd
    driver.quit()
