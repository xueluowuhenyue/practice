# -*- coding:utf-8 -*-
from Pages.basepage import BasePage
from data import locator
from time import sleep


class Home(BasePage):
    def homepage(self):
        # 左滑3次
        self.window_left(4)
        # 点击立即体验
        self.wait_click(locator.button)
        sleep(1)