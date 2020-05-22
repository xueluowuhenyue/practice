from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class BasePage:
    filename = r"D:\pycharm\ResumeTheDelivery\data\img" + str(time.time())[:5] + '.png'

    def  __init__(self,driver: Chrome):
        self.driver = driver
        self.driver.get("https://mkt.51job.com/tg/sem/pz_v2.html?from=baidupz")
        
    def wait_ele(self, locator, timeout=30, poll_frequency=0.5) -> WebElement:
        """
        :param locator: 元素定位表达式
        :param timeout: 超时时间
        :param poll_frequency: 查找频率
        :return: 返回值
        """
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            ele = wait.until(ec.presence_of_element_located((locator)))
            return ele
        except Exception as e:
            self.driver.save_screenshot(self.filename)
            raise e

    def wait_list(self, locator, timeout=30, poll_frequency=0.5) -> list:
        """
        查询多个元素
        :param locator: 元素定位表达式
        :param timeout: 超时时间
        :param poll_frequency: 查找频率
        :return: 返回元素对象的列表
        """
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            ele_list = wait.until(ec.presence_of_all_elements_located((locator)))
            return ele_list
        except Exception as e:
            self.driver.save_screenshot(self.filename)
            raise e

    def ele_click(self,locator, timeout=30, poll_frequency=0.5):
        """
        查询多个元素
        :param
        locator: 元素定位表达式
        :param
        timeout: 超时时间
        :param
        poll_frequency: 查找频率
        :return: 返回元素对象的列表
        """
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            ele = wait.until(ec.presence_of_element_located((locator)))
            return ele.click()
        except Exception as e:
            self.driver.save_screenshot(self.filename)
            raise e

    def wait_click(self, locator, timeout=30, poll_frequency=0.5):
        """
        等待元素出现并点击
        :param
        locator: 元素定位表达式
        :param
        timeout: 超时时间
        :param
        poll_frequency: 查找频率
        """
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            wait.until(ec.element_to_be_clickable((locator)))
        except Exception as e:
            self.driver.save_screenshot(self.filename)
            raise e

    def select_option(self, locator, option):
        """
        下拉框选择
        :param locator: 元素定位表达式
        :param option: 选项
        :return:
        """
        select = self.wait_ele(locator)
        ele = Select(select)
        ele.select_by_value(option)