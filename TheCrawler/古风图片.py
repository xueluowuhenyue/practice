from time import sleep

from selenium.webdriver import Chrome
from urllib.request import urlretrieve
from selenium.webdriver.chrome.options import Options

url = "http://sc.chinaz.com/tupian/ribenmeinv.html"

# 设置无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = Chrome(chrome_options=chrome_options, executable_path=r"C:\Python\Scripts\chromedriver.exe")

driver.get(url)

jCode = "window.scrollTo(0,document.body.scrollHeight);"
driver.execute_script(jCode)

sleep(5)
picture_list = driver.find_elements_by_xpath("//div[contains(@class,'imgload')]/div//img")
for i in picture_list:
    img_name = i.get_attribute("alt")
    try:
        img_path = i.get_attribute("src")
        print("正在开始下载：%s...." % img_name)
        urlretrieve(img_path, r"D:\pycharm\TheCrawler\images/"+img_name+".jpg")
    except Exception as e:
        raise e
