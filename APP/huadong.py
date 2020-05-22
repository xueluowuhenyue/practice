# -*- coding:utf-8 -*-
from appium.webdriver import Remote
# 获得机器屏幕大小x,y
driver=Remote()


# @property
def getsize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipe_up(t):
    l = getsize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 屏幕向下滑动
def swipe_down(t):
    l = getsize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 屏幕向左滑动
def swipe_left(t):
    l = getsize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    driver.swipe(x1, y1, x2, y1, t)


# 屏幕向右滑动
def swipe_right(t):
    l = getsize()
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2, y1, t)


# 调用向左滑动
swipe_left(1000)
# 调用向右滑动
swipe_right(1000)
# 调用向上滑动
swipe_up(1000)
# 调用向下滑动
swipe_down(1000)