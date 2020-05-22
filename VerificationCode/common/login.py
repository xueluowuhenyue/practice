from PIL import Image
from common.ShowapiRequest import ShowapiRequest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.driver.get('http://40.125.168.194:8080/freshingApp/login')

    def GetElement(self, locator) -> WebElement:
        wait = WebDriverWait(self.driver, 10, 0.3)
        ele = wait.until(ec.presence_of_element_located((locator)))
        return ele

    def login(self):
        self.GetElement((By.XPATH, "//input[@name='username']")).send_keys(1358634977)
        self.GetElement((By.XPATH, "//input[@name='password']")).send_keys(123456)

        # self.driver.maximize_window()
        self.driver.save_screenshot(r"D:\pycharm\VerificationCode\Picture\login.png")
        self.screenshot()  # 截取验证码
        self.GetCode()

        # 验证码输入框
        # self.GetElement((By.XPATH, "//input[@name='captcha']")).send_keys("xxxxx")
        # self.GetElement((By.XPATH, "//a")).click()

    def screenshot(self):
        picture = self.GetElement((By.XPATH, "//img"))
        loc = picture.location
        size = picture.size
        left = loc['x']
        right = loc['x']+size['width']
        upper = loc['y']
        lower = loc['y']+size['height']
        val = (left, upper, right, lower)

        loginimg = Image.open(r"D:\pycharm\VerificationCode\Picture\login.png")
        loginimg.crop(val).save(r"D:\pycharm\VerificationCode\Picture\yzm.png")

    def GetCode(self):
        r = ShowapiRequest("https://route.showapi.com/932-2", "171507", "7978022dd9ad4e7d9e2b200b60c3e1e6")
        r.addFilePara("image", r"D:\pycharm\VerificationCode\Picture\yzm.png")
        r.addBodyPara("typeId", "34")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        res = r.post().json()
        print(res)  # 返回信息


if __name__ == '__main__':
    Login(Chrome()).login()

