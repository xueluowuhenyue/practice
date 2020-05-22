# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By


# 立即体验按钮
button=(By.ID,'com.xxzb.fenwoo:id/btn_start')

# “我”按钮
I_button=(By.XPATH,'//android.widget.TabWidget[@resource-id="android:id/tabs"]/android.widget.LinearLayout[4]')

# 用户名输入框
username_input=(By.ID,'com.xxzb.fenwoo:id/et_phone')

# 下一步按钮
next_button=(By.ID,'com.xxzb.fenwoo:id/btn_next_step')

# 密码输入框
pwd_input=(By.ID,'com.xxzb.fenwoo:id/et_pwd')

# 马上设置
setting_button=(By.ID,'com.xxzb.fenwoo:id/btn_confirm')

# 创建手势密码
create_pwd=(By.ID,'com.xxzb.fenwoo:id/btn_gesturepwd_guide')

# “确定”按钮
determine=(By.ID,"com.xxzb.fenwoo:id/right_btn")

# 九宫格位置
scratchable_latex=(By.ID,'com.xxzb.fenwoo:id/gesturepwd_create_lockview')

# 定位提示
# prompt=(By.CLASS_NAME,'android.widget.LinearLayout')
