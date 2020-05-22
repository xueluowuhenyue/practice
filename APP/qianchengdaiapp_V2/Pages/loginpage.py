# -*- coding:utf-8 -*-
from Pages.basepage import BasePage
from data.locator import login_locator
from time import sleep


class Login(BasePage):
    def login(self, mobile_phone='18684720553'):
        # # 点击我
        # self.click_me()
        # sleep(3)
        # 清除登录名
        self.clear_username()
        # 输入用户名
        self.get_username_input().send_keys(mobile_phone)
        # 点击下一步
        self.click_next()
        sleep(1)

    def click_me(self):
        ' ''点击“我'' '
        self.wait_click(login_locator.button)

    def click_login(self):
        ' ''点击注册登录'' '
        self.wait_click(login_locator.login)

    def get_username_input(self):
        ' ''定位手机号码输入框'' '
        ele=self.wait_ele(login_locator.username_input)
        return ele

    def click_next(self):
        ' ''点击下一步'' '
        self.wait_click(login_locator.next_button)

    def get_password_input(self):
        ' ''定位密码输入框'' '
        ele=self.wait_ele(login_locator.pwd_input)
        return ele

    def click_talk_later(self):
        ' ''点击“以后再说”'' '
        self.wait_click(login_locator.talk_later)

    def click_set_immediately(self):
        ' ''点击马上设置'' '
        self.wait_click(login_locator.setting_button)

    def get_username(self):
        ' ''获取用户名'' '
        ele=self.wait_ele(login_locator.username)
        return ele.text

    def clear_username(self):
        ' ''清除用户名'' '
        return self.get_username_input().clear()

    def clear_password(self):
        ' '' 清除密码 '' '
        return self.get_password_input().clear()

    def popup_prompt(self):
        ' ''点击弹窗按钮'' '
        self.wait_click(login_locator.popup_button)