# -*- coding:utf-8 -*-
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class InstallApk:

    def open_app(self,Version,name,Activity,Package,Reset):
        caps={'platformName':'Android',
              'platformVersion':Version,
              'deviceName':name,
              'appActivity':Activity,
              'appPackage':Package,
              # 'app':self.app,
              'moReset':Reset}

        self.driver=Remote(desired_capabilities=caps)
        sleep(10)
        self.driver.quit()
        return self.driver

    def wait_ele(self,locator):
        Wait=WebDriverWait(self.driver,30)
        ele=Wait.until(ec.presence_of_element_located((locator)))
        return ele


if __name__ == '__main__':
    InstallApk().open_app(5.1,'Android Emulator','com.xxzb.fenwoo.activity.addition.WelcomeActivity',
               'com.xxzb.fenwoo',False)
