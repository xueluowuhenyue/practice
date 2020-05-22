# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

# 点击“注册登录”
login=(By.ID,'com.xxzb.fenwoo:id/btn_login')

# “我”按钮
button=(By.XPATH,'//android.widget.TabWidget[@resource-id="android:id/tabs"]/android.widget.LinearLayout[4]')

# 用户名输入框
username_input=(By.ID,'com.xxzb.fenwoo:id/et_phone')

# 下一步\确定按钮
next_button=(By.ID,'com.xxzb.fenwoo:id/btn_next_step')

# 密码输入框
pwd_input=(By.ID,'com.xxzb.fenwoo:id/et_pwd')

# 以后再说
talk_later=(By.ID,'com.xxzb.fenwoo:id/btn_cancel')

# 马上设置
setting_button=(By.ID,'com.xxzb.fenwoo:id/btn_confirm')

# 用户名
username=(By.ID,'com.xxzb.fenwoo:id/tv_name')

# 弹窗确定
popup_button=(By.ID,'com.xxzb.fenwoo:id/btn_confirm')