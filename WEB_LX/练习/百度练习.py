# -*- coding:utf-8 -*-
from time import sleep
from random import choice
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver=Chrome()
driver.get('https://www.baidu.com')
sleep(1)
ac=ActionChains(driver)
ele = driver.find_element_by_xpath("//a[contains(@href,'preferences')]")
ac.move_to_element(ele).perform()
ele=driver.find_element_by_xpath("//a[text()='高级搜索']")
ac.move_to_element(ele).click().perform()
# 等待窗口打开
# handled=driver.window_handles()
# WebDriverWait(driver,10).until(ec.new_window_is_opened(handled))

sleep(1)
list = driver.find_elements_by_xpath("//div[@class='result-setting']//input")
for i in list:
    if i.get_attribute('name')=='q1':
        i.send_keys('python')
    elif i.get_attribute('name')=='q2':
        i.send_keys('list')
    elif i.get_attribute('name')=='q3':
        i.send_keys('tuple')
    else:
        i.send_keys('dict')

# 选择时间最近一周
sel=driver.find_element_by_xpath("//select[@name='gpc']")
select=Select(sel)
select.select_by_index(2)
# 选择文档格式
file=driver.find_element_by_xpath("//select[@name='ft']")
file=Select(file)
file.select_by_value('doc')
# 关键字位置
locator_list=driver.find_elements_by_xpath("//td[@id='adv-setting-6']")
m=choice(locator_list)
m.click()
sleep(5)
driver.quit()


if __name__ == '__main__':
    pass