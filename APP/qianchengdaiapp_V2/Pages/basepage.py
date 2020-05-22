# -*- coding:utf-8 -*-
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from appium.webdriver import Remote
from appium.webdriver.common.mobileby import MobileBy as By
from Common.Public import project_path
import re

class BasePage:
    def __init__(self, driver: Remote):
        self.driver=driver
    # driver = Remote(desired_capabilities=devices_info.caps)

    def wait_ele(self, locator, timeout=10, poll_frequency=0.5) -> WebElement:
        '''本函数用于等待元素'''
        Wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            ele = Wait.until(ec.presence_of_element_located((locator)))
            return ele
        except Exception as e:
            self.get_screenshot()
            raise e

    # def selector_ele(self,locator):
    #     ele = WebDriverWait(self.driver, 30).until(
    #         ec.element_to_be_clickable((By.ANDROID_UIAUTOMATOR,
    #         'new uiselector().text("%s")' % locator)))
    #     return ele

    def wait_list(self, Locator, timeout=10, poll_frequency=0.5) -> list:
        '''本函数用于等待元素'''
        Wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            li = Wait.until(ec.presence_of_all_elements_located((Locator)))
            return li
        except Exception as e:
            raise e

    def wait_click(self,locator,timeout=30,poll_frequency=0.5) -> WebElement:
        '''等待元素可以点击'''
        try:
            Wait = WebDriverWait(self.driver,timeout,poll_frequency)
            ele=Wait.until(ec.element_to_be_clickable(locator))
            return ele.click()
        except Exception as e:
            raise e

    def window_size(self):
        ' ''获取屏幕尺寸'' '
        size=self.driver.get_window_size()
        width=size['width']
        height=size['height']
        return width , height

    def window_left(self, count, offset=0.1):
        ' ''左滑'' '
        for i in range(count):
            self.driver.swipe(self.window_size()[0]*(1-offset),self.window_size()[1]*0.5,
                              self.window_size()[0]*offset,self.window_size()[1]*0.5)
            sleep(1)
        # while True:
        #     try:
        #         self.wait_click(locator)
        #         break
        #     except Exception as e:
        #         self.driver.swipe(self.window_size()[0] * 0.9, self.window_size()[1] * 0.5,
        #                          self.window_size()[0]*0.1,self.window_size()[1]*0.5)
        #         sleep(1)

    def window_right(self, count, offset=0.1):
        ' ''右滑'' '
        for i in range(count):
            self.driver.swipe(self.window_size()[0]*offset,self.window_size()[1]*0.5,
                              self.window_size()[0]*(1-offset),self.window_size()[1]*0.5)
            sleep(1)

    def window_on(self, count, offset=0.1):
        ' ''上滑'' '
        for i in range(count):
            self.driver.swipe(self.window_size()[0]*0.5,self.window_size()[1]*(1-offset),
                              self.window_size()[0]*0.5,self.window_size()[1]*offset)
            sleep(1)

    def window_under(self, count, offset=0.1):
        ' ''下滑'' '
        for i in range(count):
            self.driver.swipe(self.window_size()[0]*0.5,self.window_size()[1]*offset,
                              self.window_size()[0]*0.5,self.window_size()[1]*(1-offset))
            sleep(1)

    def get_toast_text(self,prompt):
        ' ''获取弹窗提示'' '
        toast_prompt=WebDriverWait(self.driver,10,0.1).until(ec.presence_of_element_located(
            (By.XPATH, "//*[contains(@text,'%s')]" % prompt)))
        return toast_prompt.text

    def get_screenshot(self, img_path=project_path.picture_path):
        ' ''截图保存'' '
        self.driver.save_screenshot(img_path)

    def get_data(self, pattern, string):
        # 从字符串获取数据
        data = re.search(pattern, string).group()
        return data
