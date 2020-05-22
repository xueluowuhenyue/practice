# -*- coding:utf-8 -*-
from appium.webdriver.common.touch_action import TouchAction

from data import locator


def coordinate(self):
    # 获取九宫格起始坐标
    ele = self.wait_ele(locator.scratchable_latex)
    rect = ele.rect
    return rect


def element_coordinate(self, m, n):
    # 定位移动位置坐标
    start_x = int(self.coordinate()['x'])
    start_y = int(self.coordinate()['y'])
    width = int(self.coordinate()['width'])
    height = int(self.coordinate()['height'])
    point = {'x': start_x + width / 6 * m, 'y': start_y + height / 6 * n}
    return point


def get_coordinate_points(self,*args):
    # 获取所有坐标点
    a = self.element_coordinate(1,1)
    b = self.element_coordinate(3,1)
    c = self.element_coordinate(5,1)
    d = self.element_coordinate(1,3)
    e = self.element_coordinate(3,3)
    f = self.element_coordinate(5,3)
    g = self.element_coordinate(1,5)
    h = self.element_coordinate(3,5)
    i = self.element_coordinate(5,5)

    list=[]
    for k in args:
        if k == 1:
            list.append(a)
        elif k == 2:
            list.append(b)
        elif k == 3:
            list.append(c)
        elif k == 4:
            list.append(d)
        elif k == 5:
            list.append(e)
        elif k == 6:
            list.append(f)
        elif k == 7:
            list.append(g)
        elif k == 8:
            list.append(h)
        else:
            list.append(i)
    return list


def move_coordinate(self):
    # 连接坐标点
    touch = TouchAction(self.driver)
    while self.
    touch.press(**self.element_coordinate(3, 1)).wait(200).move_to(**self.element_coordinate(1, 3)).wait(200).move_to(
        **self.element_coordinate(3, 5)).wait(200).move_to(**self.element_coordinate(5, 3)).wait(200).move_to(
        **self.element_coordinate(3, 1)).release().perform()