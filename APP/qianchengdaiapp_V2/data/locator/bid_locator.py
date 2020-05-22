# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

# 项目按钮
# project=(By.CLASS_NAME, 'android.widget.LinearLayout')
project=(By.XPATH, '//android.widget.TabWidget[@resource-id="android:id/tabs"]/android.widget.LinearLayout[2]')

# 选择项目
bid_ele=(By.XPATH, '//android.widget.ListView[@resource-id="com.xxzb.fenwoo:id/lv_loan"]/android.widget.RelativeLayout[1]')  # class android.widget.ListView

# 投资框
bid_input=(By.ID, 'com.xxzb.fenwoo:id/et_investamount')

#  投资按钮
bid_button=(By.ID, 'com.xxzb.fenwoo:id/btn_investnow')

# 返回按钮
return_button=(By.ID, 'com.xxzb.fenwoo:id/btn_back')

# 成功提示
success_msg=(By.ID, 'com.xxzb.fenwoo:id/tv_title')

# 确定按钮
determine_button=(By.ID, 'com.xxzb.fenwoo:id/btn_confirm')

# “我”按钮
button=(By.XPATH,'//android.widget.TabWidget[@resource-id="android:id/tabs"]/android.widget.LinearLayout[4]')

# 余额
leave_amount=(By.ID,'com.xxzb.fenwoo:id/tv_leave')