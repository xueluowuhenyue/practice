#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 14:51
# @Author  : Xuegod Teacher For
# @File    : 02_get_song_url_test.py
# @Software: PyCharm

from selenium import webdriver
import time
#动作练，鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
#显示等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#http库
from urllib import request

driver = webdriver.Chrome()

def get_song_url():
    '''
    :return: 歌曲的URL地址
    '''
    qq_url = 'https://y.qq.com/'
    driver.get(qq_url)
    #隐式等待，智能等待
    driver.implicitly_wait(10)
    #强制等待
    # time.sleep(10)
    #显示等待0-10
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,'popup__icon_close')))

    driver.find_element_by_class_name('popup__icon_close').click()

    time.sleep(2)
    #将鼠标悬停到当前的标签
    button = driver.find_element_by_class_name('search_input__btn')
    ActionChains(driver).move_to_element(button).perform()
    #进行输入并点击
    driver.find_element_by_class_name('search_input__input').send_keys('说好不哭')
    time.sleep(0.3)
    button.click()

    song_url = driver.find_element_by_class_name('songlist__songname_txt').find_element_by_tag_name('a').get_attribute('href')

    print('你所要下载的歌曲地址:',song_url)

    return song_url

def down_song(song_url):

    js = 'window.open("http://www.douqq.com/qqmusic/")'
    driver.execute_script(js)
    #当前你程序操作的窗口句柄
    QQ_handle = driver.current_window_handle
    #所有句柄
    handles = driver.window_handles

    # print(handles)
    driver.switch_to.window(handles[-1])

    driver.find_element_by_id('mid').send_keys(song_url)
    driver.find_element_by_id('sub').click()

    time.sleep(1)

    print('正在输入mp3地址')
    mp3_url = driver.find_element_by_id('mp3_h').text

    if mp3_url:
        print('正在下载……')
        #下载网站数据
        request.urlretrieve(mp3_url,'说好不哭.mp3')

    else:
        print('没有获取到地址')
    print('完毕')
    #退出浏览器
    driver.quit()




if __name__ == '__main__':
    song_url = get_song_url()
    down_song(song_url)