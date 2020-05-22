# -*- coding:utf-8 -*-
from Pages.basepage import BasePage
from data.locator import bid_locator
from time import sleep


class Bid(BasePage):
    ' ''投标页面'' '
    def the_tender(self, money):
        # 进入项目页面
        self.click_project()
        sleep(1)
        # 选择投资项目
        self.click_bid_project()
        sleep(3)
        # 获取余额
        amount = self.get_money('[1-9][0-9]+')
        print(amount)
        # 清空输入框
        # self.clear_input()
        # 输入投资金额
        self.get_bid_input().send_keys(money)
        # 点击立即投标
        self.click_bid_button()
        return amount

    def click_project(self):
        # 项目按钮
        ele = self.wait_ele(bid_locator.project)
        return ele.click()

    def click_bid_project(self):
        ' ''获取项目'' '
        ele=self.wait_ele(bid_locator.bid_ele)
        return ele.click()

    def get_bid_input(self):
        ' ''定位输入框'' '
        ele=self.wait_ele(bid_locator.bid_input)
        return ele

    def clear_input(self):
        ' ''清空输入框'' '
        return self.get_bid_input().clear()

    def click_bid_button(self):
        ' ''点击投资'' '
        return self.wait_click(bid_locator.bid_button)

    def click_back(self):
        '''点击返回'''
        return self.wait_click(bid_locator.return_button)

    def click_user(self):
        ' ''点击我的'' '
        return self.wait_click(bid_locator.button)

    def get_money(self, pattern):
        ' ''获取余额'' '
        ele=self.get_bid_input()
        return int(self.get_data(pattern, ele.text))

    def get_leave_amount(self):
        ' ''获取投资后的余额'''
        ele=self.wait_ele(bid_locator.leave_amount)
        s=ele.text
        money=s.replace(',', '')           # 去掉逗号
        return int(float(money))

    def get_msg(self):
        ' ''获取投资活动提示'' '
        ele=self.wait_ele(bid_locator.success_msg)
        return ele.text

    def click_determine(self):
        ' ''点击确定'' '
        return self.wait_click(bid_locator.determine_button)


if __name__ == '__main__':
    Bid().the_tender(1515)