from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import time,sleep
driver=Chrome()
driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d9UBZ8i0&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F')
driver.implicitly_wait(10)
# def Wait(method,value) -> WebElement:
#     '''该函数实现显性等待功能'''
#     wait=WebDriverWait(driver,10,0.3)
#     ele=wait.until(ec.presence_of_element_located((method,value)))
#     return ele
# ele=Wait(By.ID,'train_date')
#修改日期
# js_code="ele=document.getElementById('train_date')"
# e=driver.execute_script(js_code)
# sleep(2)
# js_code2="ele.readOnly=false"
# driver.execute_script(js_code2)
# sleep(2)
# js_code3="ele.value='2019-05-15'"
# driver.execute_script(js_code3)
# sleep(3)
driver.find_element_by_xpath("//a[text()='密码登录']").click()
driver.find_element_by_xpath("//input[@id='TPL_username_1']").send_keys('yonghuming')
sleep(2)
