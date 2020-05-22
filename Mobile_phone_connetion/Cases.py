from time import sleep
from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import yaml

caps = yaml.load(open(r"D:\Pycharm\Scripts\Mobile_phone_connetion\Data\device_info.yaml",encoding='utf-8'),
                 Loader=yaml.FullLoader)
# print(caps)
driver = Remote(desired_capabilities=caps)


def get_size():
    """获取屏幕尺寸"""
    size = driver.get_window_size()
    return size


width = get_size()['width']
height = get_size()['height']


def swipe_left(num):
    """滑屏操作"""
    for i in range(num):
        driver.swipe(width*0.9,height*0.1,width*0.1,height*0.1)
        sleep(1)


def get_local(locator) -> WebElement:
    """元素定位"""
    wait=WebDriverWait(driver,timeout=30, poll_frequency=0.3)
    ele = wait.until(ec.presence_of_element_located(locator))
    return ele


# 滑屏
swipe_left(4)
# 点击“体验
# driver.tap([(550, 1850)], 100)
get_local((MobileBy.ID, 'com.xxzb.fenwoo:id/btn_start')).click()
sleep(120)
# # 点击“我”的
# get_local((MobileBy.XPATH, '//android.widget.TabWidget[@resource-id="android:id/tabs"]/android.widget.LinearLayout[4]'))
# # 输入手机号码   'mobile': '18684720553','pwd': 'python'
# get_local((MobileBy.ID,'com.xxzb.fenwoo:id/et_phone')).send_keys('18684720553')
# # 点击“下一步”
# get_local((MobileBy.ID,'com.xxzb.fenwoo:id/btn_next_step')).click()
# # 输入密码
# get_local((MobileBy.ID,'com.xxzb.fenwoo:id/et_pwd')).send_keys('python')
# # 下一步\确定按钮
# get_local((MobileBy.ID, 'com.xxzb.fenwoo:id/btn_next_step')).click()
# sleep(1)
# # 点击“马上设置”
# get_local((MobileBy.ID,'com.xxzb.fenwoo:id/btn_confirm')).click()
# # 点击“创建手势密码”
# get_local((MobileBy.ID,'com.xxzb.fenwoo:id/btn_gesturepwd_guide')).click()
# # 点击确定
# get_local((MobileBy.ID,"com.xxzb.fenwoo:id/right_btn")).click()
# # 九宫格定位
# ele = get_local((MobileBy.ID,'com.xxzb.fenwoo:id/gesturepwd_create_lockview'))
# rect = ele.rect
# # 图片大小
# wdt = rect['width']
# hgt = rect['height']
# x = rect['x']
# y = rect['y']


# def lock_screen():
#     num_1 = {'x': x + wdt / 6 * 1, 'y': y + hgt / 6 * 1}
#     num_2 = {'x': x + wdt / 6 * 3, 'y': y + hgt / 6 * 1}
#     num_3 = {'x': x + wdt / 6 * 5, 'y': y + hgt / 6 * 1}
#     num_4 = {'x': x + wdt / 6 * 1, 'y': y + hgt / 6 * 3}
#     num_5 = {'x': x + wdt / 6 * 3, 'y': y + hgt / 6 * 3}
#     num_6 = {'x': x + wdt / 6 * 5, 'y': y + hgt / 6 * 3}
#     num_7 = {'x': x + wdt / 6 * 1, 'y': y + hgt / 6 * 5}
#     num_8 = {'x': x + wdt / 6 * 3, 'y': y + hgt / 6 * 5}
#     num_9 = {'x': x + wdt / 6 * 5, 'y': y + hgt / 6 * 5}
#     tc = TouchAction(driver)
#     tc.press(**num_1).wait(300).move_to(**num_2).wait(300).move_to(**num_3).wait(300).move_to(**num_4).wait(300).move_to(
#         **num_7).wait(300).move_to(**num_8).wait(300).move_to(**num_9).wait(300).release().perform()
#
#
# lock_screen()
# sleep(30)


if __name__ == '__main__':
    driver.quit()