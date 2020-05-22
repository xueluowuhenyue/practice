#--*--
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome, ActionChains
from time import time,sleep
driver=Chrome()
def wait(methed,ele,num=1) -> WebElement:
    Wait=WebDriverWait(driver,10,0.2)
    if num==1:
        ele=Wait.until(ec.presence_of_element_located((methed,ele)))
    else:
        ele=Wait.until(ec.presence_of_all_elements_located((methed,ele)))
    return ele
#定位出发地输入框
ac=ActionChains(driver)
driver.get('https://www.12306.cn/index/')
code="e=document.getElementById('fromStationText')"
driver.execute_script(code)
sleep(2)
value="e.value='成都'"
driver.execute_script(value)
ac.send_keys(Keys.ENTER)
#定位目的地输入框
code="ele=document.getElementById('toStationText')"
driver.execute_script(code)
sleep(2)
value="ele.value='达州'"
driver.execute_script(value)
ac.send_keys(Keys.ENTER)
# 定位日期输入框
code="ele=document.getElementById('train_date')"
e=driver.execute_script(code)
sleep(2)
#修改readonly为false
set="ele.readOnly=false"
driver.execute_script(set)
sleep(2)
#修改日期
data="ele.value='2019-05-15'"
driver.execute_script(data)
#点击查询
wait(By.XPATH,"//a[@id='search_one']").click()

# ac=ActionChains(driver)
# ele=wait(By.ID,'fromStationText')
# ac.move_to_element(ele).click(ele).perform()
# ac.send_keys("成都").perform()
# sleep(1)
# e=wait(By.XPATH,"//*[@id='panel_cities']//*[text()='成都']")
# ac.move_to_element(e).click(e).perform()
# ac.send_keys(Keys.ENTER)
# # e.click()
# # ele=wait(By.ID,'fromStationText')
# # ac.move_to_element(ele).perform()
# # ac.click()
# ac.send_keys("达州").perform()
# sleep(1)
# b=wait(By.XPATH,"//*[@id='panel_cities']//*[text()='达州']")
# ac.move_to_element(b).click(b).perform()
# ac.send_keys(Keys.ENTER)
#
# ele=wait(By.ID,'search_one')
# ac.move_to_element(ele).click(ele).perform()