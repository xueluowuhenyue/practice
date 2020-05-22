# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys
# from lxml import etree


class downloader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'https://www.biqukan.com/1_1680/'
        self.names = []            # 存放章节名
        self.urls = []            # 存放章节链接
        self.nums = 0            # 章节数

    def get_download_url(self):
        req = requests.get(url = self.target)
        req.encoding='gbk'
        html = req.text
        div_bf = BeautifulSoup(html,features="lxml")
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),features="lxml")
        a = a_bf.find_all('a')
        self.nums = len(a[15:])     # 剔除不必要的章节，并统计章节数
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url = target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html,features="lxml")
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《凡人修仙之仙界篇》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '凡人修仙之仙界篇.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《凡人修仙之仙界篇》下载完成')