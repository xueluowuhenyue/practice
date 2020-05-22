# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from Pages.basepage import BasePage
from data import locator
from time import sleep

# 立即体验按钮
button=(By.ID,'com.xxzb.fenwoo:id/btn_start')


class Home(BasePage):
    def homepage(self):
        # 左滑3次
        self.window_left(4)
        # 点击立即体验
        self.wait_click(button)
        sleep(1)