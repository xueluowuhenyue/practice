import requests
from lxml import etree
from urllib.request import urlretrieve

base_url = "http://www.521609.com"
headers = {'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

start = int(input("请输入开始位置：》》》"))
end = int(input("请输入结束的位置：》》》"))
for i in range(start+30, end+31):
    response = requests.get(f"http://www.521609.com/daxuexiaohua/list{i}.html", headers=headers)
    context = response.content.decode("gbk")
    html = etree.HTML(context)

    # 图片定位：//div[contains(@class,'index_img')]//img/ancestor::li  //div[contains(@class,'index_img')]//img
    # 图片列表
    picture_list = html.xpath("//div[contains(@class,'index_img')]//img")
    # print(picture_list)

    for i in picture_list:
        # 获取图片地址
        img_path = i.xpath("./@src")[0]
        # 获取图片名称
        img_name = i.xpath("./@alt")[0]
        # print(img_name, img_path)
        url = base_url + img_path
        # print(url)
        print("正在开始下载：%s...." % img_name)
        urlretrieve(url, r"D:\pycharm\TheCrawler\images/"+img_name+".jpg")