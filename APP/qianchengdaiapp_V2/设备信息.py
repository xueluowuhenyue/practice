# -*- coding:utf-8 -*-
# from yaml import load
# import re
from appium.webdriver import Remote
caps = {'platformName': 'Android',                                           # 操作系统
                'platformVersion': 5.1,                                      # 版本
                'deviceName': 'Android Emulator',
                'appActivity':'com.xxzb.fenwoo.activity.addition.WelcomeActivity',    # 入口
                'appPackage': 'com.xxzb.fenwoo',                            # 包名
                # 'app':r'E:\V1.2.2\app-release.apk',                        # 文件路径
                'automationName':'UiAutomator2',
                'noReset': False}                                            # 重置
driver = Remote(desired_capabilities=caps)

mg=driver.current_activity
print(mg)
# path=r'D:\pycharm-professional-2019.1.1\APP\qianchengdaiapp_V2\a.yaml'
# m=load(open(path))
#
# print(m)

# s='可用余额35451.48元'
#
# p = '[1-9][0-9]+'
#
# m=re.search(p,s).group()
# print(m)
#
# s='34,301.05'
# for i in s:
#     if i == ',':
#         s1=s.replace(i, '')
#         print(s1)
# m= s.replace(',', '')
#
# print(int(float(m)))
#
# a='3.21'
# print(int(float(a)))