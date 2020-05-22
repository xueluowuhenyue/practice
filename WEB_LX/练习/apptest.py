from time import sleep
from appium.webdriver import Remote
caps = {'platformName': 'Android',                                           # 操作系统
                'platformVersion': 5.1,                                      # 版本
                'deviceName': 'Android Emulator',
                'appActivity':'com.hkq.ctrl.app.ui.login.SplashActivity',    # 入口
                'appPackage': 'com.hkq.ctrl.app',                            # 包名
                'app':r'C:\freshingair1.2.5.apk',                        # 文件路径
                'automationName':'UiAutomator2',
                'noReset': False}                                            # 重置
driver = Remote(desired_capabilities=caps)
sleep(10)
# android_uiautomator文本元素定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("手机号")').send_keys("freshingair")
driver.find_element_by_accessibility_id("com.hkq.ctrl.app:id/et_login_userName").send_keys("freshingair")

# android_uiautomator元素id定位
ele=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hkq.ctrl.app:id/et_login_pwd")')
ele.send_keys("123456")
# driver.find_element_by_android_uiautomator('new UiSelector().text("登录")')
# tap点击
# driver.find_element_by_class_name("android.widget.Button")
driver.tap([(442,548)],300)