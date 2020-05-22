# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.common.touch_action import TouchAction
from Pages.basepage import BasePage
from data import locator
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Pwd(BasePage):
    def create_pwd(self):
        # 点击马上设置
        self.wait_click(locator.setting_button)
        # 点击创造手势密码
        self.wait_click(locator.create_pwd)
        sleep(3)
        # 点击确定按钮
        self.wait_click(locator.determine)
        # 设置密码
        self.move()
        # 点击继续按钮
        self.wait_click(locator.determine)
        # 密码确认
        self.move()
        # 点击确定按钮
        self.wait_click(locator.determine)
        # self.driver.reset()
        # self.move()

    def coordinate(self):
        # 获取九宫格起始坐标
        ele=self.wait_ele(locator.scratchable_latex)
        rect=ele.rect
        return rect

    def element_coordinate(self,a,b):
        # 定位移动位置坐标
        start_x=int(self.coordinate()['x'])
        start_y = int(self.coordinate()['y'])
        width=int(self.coordinate()['width'])
        height = int(self.coordinate()['height'])
        point={'x':start_x + width/6*a,'y':start_y + height/6*b}
        return point

    def move(self):
        # 设置手势密码
        touch=TouchAction(self.driver)
        touch.press(**self.element_coordinate(3,1)).wait(200).move_to(**self.element_coordinate(1,3)).wait(200).move_to(
            **self.element_coordinate(3,5)).wait(200).move_to(**self.element_coordinate(5,3)).wait(200).move_to(
            **self.element_coordinate(3,1)).release().perform()

    def get_toast_text(self,text):
        # try:
        #     toast_loc = (By.XPATH, "//*[contains(@text,'" + text + "')]")
        #     ele = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
        #     return ele.text
        # except Exception as e:
        #     print('获取提示失败')
        #     raise e
        toast_text=WebDriverWait(self.driver,10,0.1).until(ec.presence_of_element_located(
            (By.XPATH, "//*[contains(@text,'%s')]" % text)))
        return toast_text.text