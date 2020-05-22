# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from unittest import TestCase

driver=Firefox()
driver.get("https://www.12306.cn/index")
sleep(5)
# 修改日期
code="ele=document.querySelector('#train_date');ele.readOnly='False';ele.value='2019-09-10';"
driver.execute_script(code)
# 填写出发点
sleep(2)
ele=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'fromStationText')))
ele.click()
ele.send_keys('成都')
ele=driver.find_element_by_xpath("//div[@id='panel_cities']//span[text()='成都']")
ac=ActionChains(driver)
ac.move_to_element(ele).click().perform()
# driver.find_element_by_xpath("//div[@id='panel_cities']//span[text()='成都']").click()
# # 目的地
ele=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'toStationText')))
ele.send_keys('达州')
# driver.find_element_by_xpath("//div[@id='panel_cities']//span[text()='达州']").click()
ele=driver.find_element_by_xpath("//div[@id='panel_cities']//span[text()='达州']")
ac=ActionChains(driver)
ac.move_to_element(ele).click().perform()
# # 点击查询
driver.find_element_by_css_selector("#search_one").click()
sleep(3)
window_list=driver.window_handles
print(window_list)
driver.switch_to.window(window_list[-1])
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
e=driver.find_elements_by_xpath('//*[@id="queryLeftTable"]//td[10][@class]/../td[1]//a')
for i in e:
    print(i.text)
# # 窗口切换
# win_list=driver.window_handles
# driver.switch_to.window(win_list[-1])
# 地址获取
# url=driver.current_url
# print(url)
# # 断言
# TestCase.assertEqual(TestCase(), driver.title, '中国铁路12306')    # 标题断言
# TestCase.assertTrue(TestCase(), 'kyfw.12306.cn' in url)              # url断言
# TestCase.assertIn(TestCase(), 'kyfw.12306.cn', url)

# driver.quit()


if __name__ == '__main__':
    pass