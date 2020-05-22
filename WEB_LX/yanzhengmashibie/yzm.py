from time import sleep
from PIL import Image
from selenium.webdriver import Chrome
from WEB_LX.yanzhengmashibie.yzm_shibie import read_yzm
from unittest import TestCase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get('http://40.125.168.194:8080/freshingApp/login')

driver.maximize_window()
driver.find_element_by_xpath("//input[@name='username']").send_keys('admin')
driver.find_element_by_xpath("//input[@name='password']").send_keys('test')
sleep(1)
ele=driver.find_element_by_xpath("//input[@name='captcha']")

driver.save_screenshot(r"D:\Pycharm\Scripts\WEB_LX\data\log.png")  # 截取屏幕内容，保存到本地

# 选择验证码元素
yam=driver.find_element_by_xpath("//img[@id='captcha']")
# 获取图片元素位置
loc= yam.location
# 获取图片大小
size = yam.size
# 获取验证码位置
left = loc['x']*1.25
right = (loc['x']+size['width'])*1.25
upper = loc['y']*1.25
lower = (loc['y']+size['height'])*1.25
val = (left,upper,right,lower)
log_img=Image.open(r'D:\Pycharm\Scripts\WEB_LX\data\log.png')

yzm_pic=log_img.crop(val)
yzm_pic.save(r'D:\Pycharm\Scripts\WEB_LX\data\yzm.png')

# 获取验证码
yzm=read_yzm("https://route.showapi.com/932-2", 34,
                    r'D:\Pycharm\Scripts\WEB_LX\data\yzm.png')
print(yzm)
# 输入验证码
driver.find_element_by_name("captcha").send_keys(yzm)
driver.find_element_by_xpath("//a[text()='登录']").click()
sleep(3)
driver.minimize_window()
driver.find_element_by_xpath("//span[text()='安全退出']").click()
# 定位弹框
driver.find_element_by_xpath("//span[text()='确定']").click()
# alert=driver.switch_to.alert
# 点击确定
# print(alter.text)
# alert.accept()
sleep(1)
url=driver.current_url
curl='http://40.125.168.194:8080/freshingApp/login'
TestCase.assertEqual(TestCase(),url,curl)
sleep(3)
driver.quit()


if __name__ == '__main__':
    pass