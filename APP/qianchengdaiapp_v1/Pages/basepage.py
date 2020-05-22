# -*- coding:utf-8 -*-
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


class BasePage:
    def __init__(self,driver):
        self.driver=driver
    # driver = Remote(desired_capabilities=devices_info.caps)

    def wait_ele(self, locator, timeout=10, poll_frequency=0.5) -> WebElement:
        '''本函数用于等待元素'''
        Wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            ele = Wait.until(ec.presence_of_element_located((locator)))
            return ele
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

    def window_left(self,count):
        ' ''左滑'' '
        for i in range(count):
            self.driver.swipe(self.window_size()[0]*0.9,self.window_size()[1]*0.5,
                              self.window_size()[0]*0.1,self.window_size()[1]*0.5)
            sleep(1)
        # while True:
        #     try:
        #         self.wait_click(locator)
        #         break
        #     except Exception as e:
        #         self.driver.swipe(self.window_size()[0] * 0.9, self.window_size()[1] * 0.5,
        #                          self.window_size()[0]*0.1,self.window_size()[1]*0.5)
        #         sleep(1)

    def window_right(self,count):
        ' ''右滑'' '
        for i in range(count):
            self.driver.swipe(self.window_size()[0]*0.1,self.window_size()[1]*0.5,
                              self.window_size()[0]*0.9,self.window_size()[1]*0.5)
            sleep(1)

    def window_on(self,count):
        ' ''上滑'' '
        for i in range(count):
            self.driver.swipe(self.window_size()[0]*0.5,self.window_size()[1]*0.9,
                              self.window_size()[0]*0.5,self.window_size()[1]*0.1)
            sleep(1)

    def window_under(self,count):
        ' ''下滑'' '
        for i in range(count):
            self.driver.swipe(self.window_size()[0]*0.5,self.window_size()[1]*0.1,
                              self.window_size()[0]*0.5,self.window_size()[1]*0.9)
            sleep(1)

