# -*- coding:utf-8 -*-
from Pages.basepage import BasePage
from data import locator, user_info
from time import sleep


class Login(BasePage):
    def login(self):
        # 点击我
        self.wait_click(locator.I_button)
        # 定位用户名输入框
        ele=self.wait_ele(locator.username_input)
        # 输入用户名
        ele.send_keys(user_info.user_name)
        # 点击下一步
        self.wait_click(locator.next_button)
        sleep(1)
        # 定位密码输入框、输入密码
        self.wait_ele(locator.pwd_input).send_keys(user_info.paword)
        # 点击“确定”
        self.wait_click(locator.next_button)
        sleep(3)