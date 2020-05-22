# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from random import choice
from time import time,sleep
driver=Chrome()
driver.implicitly_wait(10)

def wait(method,ele,num=1) ->WebElement:
    Wait=WebDriverWait(driver,10)
    if num==1:
        e=Wait.until(ec.presence_of_element_located((method,ele)))
    else:
        e=Wait.until(ec.presence_of_all_elements_located((method,ele)))
    return e
def baidu():
    '''定位百度首页-设置-高级设置'''
    driver.get('https://www.baidu.com/')
    # wait(By.XPATH,"//a[text()='设置' and contains(@href,'http')]").click()
    # wait(By.XPATH,"//*[text()='高级搜索']").click()
    # 创建一个新的动作链。
    ac=ActionChains(driver)
    # 定位设置元素
    ele=wait(By.XPATH,"//a[text()='设置' and contains(@href,'http')]")
    ac.move_to_element(ele).perform()
    #点击设置
    ac.click().perform()
    #移动鼠标到高级搜索
    # e=wait(By.XPATH,"//*[text()='高级搜索']")
    ac.move_to_element(wait(By.XPATH,"//*[text()='高级搜索']")).perform()
    ac.click().perform()
    #定位输入框，输入内容
    in_list=wait(By.XPATH,"//*[@class='result-setting']//input",2)
    for i in in_list:
        if i.get_attribute("name")=="q1":
            i.send_keys('1')
        elif i.get_attribute("name")=="q2":
            i.send_keys('2')
        elif i.get_attribute("name")=="q3":
            i.send_keys('3')
        else:
            i.send_keys('4')
    #下拉框选择
    select=wait(By.XPATH,"//*[@name='ft']")
    from selenium.webdriver.support.select import Select
    ele=Select(select)
    # 索引
    # ele.select_by_index(2)
    #根据值
    ele.select_by_value("xls")
    #文本
    # ele.select_by_visible_text("所有格式")
    se_list=wait(By.XPATH,"//*[@id='adv-setting-6']/input",2)
    ele=choice(se_list)
    ele.click()
    sleep(3)
    driver.quit()
def set_data():
    '''定位日期输入框'''
    driver.get('https://www.12306.cn/index/')
    code="ele=document.getElementById('train_date')"
    driver.execute_script(code)
    sleep(2)
    #修改readonly为false
    set="ele.readOnly=false"
    driver.execute_script(set)
    sleep(2)
    #修改日期
    data="ele.value='2019-05-15'"
    driver.execute_script(data)
    sleep(3)
    driver.quit()
def txkt():
    ''' 腾讯课堂QQ登录'''
    driver.get('https://ke.qq.com/')
    # 点击登录
    wait(By.ID,'js_login').click()
    #选择QQ登录
    wait(By.XPATH,"//a[@class='js-btns-enter btns-enter btns-enter-qq']").click()
    #切换iframe
    driver.switch_to.frame('login_frame_qq')
    #选择账号密码登录
    wait(By.XPATH,"//a[text()='帐号密码登录']").click()
    #截屏
    sleep(1)
    driver.save_screenshot('login.png')
    driver.quit()

def ketpai():
    '''课堂派打印二维码'''
    driver.get('https://www.ketangpai.com')
    #点击登录
    wait(By.CLASS_NAME,'login').click()
    #点击微信登录
    wait(By.XPATH,"//a[contains(text(),'微信')]").click()
    # 获取iframe的WebElement对象
    ele=wait(By.XPATH,"//iframe[contains(@src,'https')]")
    #切换到iframe
    driver.switch_to.frame(ele)
    #定位二维码
    ele=wait(By.XPATH,"//img[contains(@class,'qrcode')]")
    #打印元素
    print(ele)
    driver.quit()
if __name__ == '__main__':
    baidu()
    # set_data()
    # txkt()
    # ketpai()