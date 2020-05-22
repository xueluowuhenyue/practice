#  -*- coding:utf-8 -*-
import pytest
from time import sleep


@pytest.mark.success
def test_add_pwd(init_pwd):
    driver=init_pwd[0]
    home=init_pwd[2]
    login=init_pwd[1]
    pwd=init_pwd[3]
    # 进入首页
    home.homepage()
    # 登录用户
    login.login()
    # 创建手势密码
    pwd.create_pwd()
    # 获取提示
    prompt=pwd.get_toast_text('设置成功')
    sleep(1)
    print(prompt)
    try:
        assert ('手势密码设置成功'== prompt)
    except AssertionError as e:
        print('断言出错啦')
        raise e
    # driver.lock()
    # driver.unlock()
    # print(driver.current_package)
    # print(driver.current_activity)
    # print(driver.current_context)
    # print(driver.page_source)
    # print(driver.device_time)
    # print(driver.desired_capabilities)
    # sleep(10)


if __name__ == '__main__':
   pytest.main()