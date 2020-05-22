# -*- coding:utf-8 -*-
# 1. 在课堂派网站上完成滚动操作2. 再课堂派网站上完成文件上传操作
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=Chrome()

def wait(method,ele) ->WebElement:
    Wait=WebDriverWait(driver,10,0.3)
    e=Wait.until(ec.presence_of_element_located((method,ele)))
    return e
def ketpai():
    '''滑动条处理'''
    driver.get('https://www.ketangpai.com')
    #定位元素”
    ele=wait(By.XPATH,"//h3[text()='作业查重杜绝抄袭']")
    sleep(1)
    #滚动页面到元素位置
    driver.execute_script("arguments[0].scrollIntoView(false);",ele)
    sleep(2)
    #滚动到底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)
    #滚动到顶部
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
    sleep(3)
    driver.quit()
if __name__ == '__main__':
    ketpai()
