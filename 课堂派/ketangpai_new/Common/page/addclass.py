from selenium.webdriver.common.by import By
from Common.page.login import Login


class AddCalss:

    def add_calss(self,data):
        # 点击加入班级
        Login().wait(By.XPATH,"//*[text()='加入班级' and contains(@class,'ktcon1l')]").click()
        # 定位输入框
        ele=Login().wait(By.XPATH,"//*[@class='chuangjiankccon']/input")
        # 输入验证码
        ele.send_keys(data)
        # 点击加入按钮
        Login().wait(By.XPATH,"//*[@class='cjli2']/a").click()