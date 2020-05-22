from time import sleep
import random
import requests
import re
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

base_url = "https://www.zhaishuyuan.com/"

# 设置无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = Chrome(chrome_options=chrome_options, executable_path=r"C:\Python\Scripts\chromedriver.exe")
jCode = "window.scrollTo(0,document.body.scrollHeight);"
file = open(r"D:\pycharm\TheCrawler\小说\万界帝主.txt", "a", encoding="utf-8")
# driver = Chrome()
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"}


def get_url():
    """获取章节数量"""

    url = "https://m.zhaishuyuan.com/read/36420"

    driver.get(url)
    ele_list = get_element(By.XPATH, "//div[@class='border-line']/parent::ul//a")
    return len(ele_list)


def download():
    driver.get("https://www.zhaishuyuan.com/chapter/36420/22492164")

    for i in range(1, 99):
        title = driver.find_element_by_xpath("//div[@class='title']//em").text

        print("正在下载：%s....." % title)
        file.write(title)
        file.write("\n")
        driver.execute_script(jCode)
        data_list = get_element(By.XPATH, "//div[@id='content']//p")
        for j in data_list:
            file.write(j.text)
            file.write("\n")
        driver.find_element_by_xpath("//div[@class='jump']//a[text()='下一章']").click()
        sleep(1)
    file.close()
    driver.quit()


def get_element(method, locator) -> list:
    """获取列表"""
    wait = WebDriverWait(driver, 10, 0.3)
    ele_list = wait.until(ec.presence_of_all_elements_located((method, locator)))
    return ele_list


if __name__ == '__main__':
    download()
    # get_url()