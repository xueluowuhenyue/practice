
# from time import sleep
#
# from selenium.webdriver import Chrome
#
# driver=Chrome()
# driver.get('https://www.12306.cn/index/')
# sleep(1)
#
# js_code="window.scrollTo(0,500)"
# driver.execute_script(js_code)
# sleep(3)
# # 滚动到底部
# js_code_2="window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js_code)
# sleep(3)
# # 滚动到顶部
# driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
# sleep(3)
# # 滚动到元素位置
# ele=driver.find_element_by_xpath("//h2[text()='友情链接']")
# # ele.location_once_scrolled_into_view()
# driver.execute_script("arguments[0].scrollIntoView(false);",ele)
