from time import sleep
from yaml import load
from appium.webdriver import Remote
from Common import Project_path
from Common.Keys import keys
caps=load(open(Project_path.device_path, encoding='utf-8'))

driver=Remote(desired_capabilities=caps)
sleep(8)
# sleep(3)
ele=driver.find_element_by_id('com.android.browser:id/url')
ele.clear()
ele.send_keys('http://www.baidu.com')
# 点击回车
driver.press_keycode(keys.KEYCODE_ENTER)
sleep(2)
context=driver.contexts
print(context)
driver.switch_to.context(context[1])
sleep(10)
ele=driver.find_element_by_id('index-kw')
ele.clear()
ele.send_keys('无上皇座')
driver.press_keycode(keys.KEYCODE_ENTER)
sleep(3)
driver.find_element_by_xpath("//span[text()='最新章节免费阅读_百度小说']").click()
