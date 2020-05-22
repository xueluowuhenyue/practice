from selenium.webdriver.common.by import By
from Common.page.login import Login
from selenium.webdriver import ActionChains
from time import sleep


class SubCalss:

    def sub_class(self,class_name,password):
        #定位三个点
        ele=Login().wait(By.XPATH,"//*[@id='viewer-container-lists']//*[@title='%s']/parent::strong/following-sibling::a" % class_name)
        ele.click()
        #选择退课
        # Login().wait(By.XPATH,"//*[@data-id='MDAwMDAwMDAwMLOsuZmHz9Fo']//a[text()='退课']").click()
        ac=ActionChains(Login().driver)
        ele=Login().wait(By.XPATH,"//*[@id='viewer-container-lists']//*[@title='%s']/parent::strong/following-sibling::ul//*[text()='退课']" %class_name)
        ac.move_to_element(ele).click(ele).perform()
        #输入密码
        Login().wait(By.XPATH,"//*[@class='deletekccon']//input").send_keys(password)
        #点击退课
        Login().wait(By.XPATH,"//*[@class='deletekt']//*[text()='退课']").click()

if __name__ == '__main__':
    SubCalss().sub_class('py14期考核','123456')