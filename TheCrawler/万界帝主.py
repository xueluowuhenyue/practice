import requests
from lxml import etree


base_url = "https://www.zhaishuyuan.com"
file = open(r"D:\pycharm\TheCrawler\小说\万界帝主.txt", "a", encoding="utf-8")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"}


def get_url():
    """获取章节地址"""
    ulist=[]
    url = "https://m.zhaishuyuan.com/read/36420"
    response = requests.get(url, headers=headers)
    context = response.content.decode("gbk")
    html = etree.HTML(context)
    href_list = html.xpath("//div[@class='border-line']/parent::ul//a")
    for i in range(len(href_list)):
        ndict = {}
        ndict["name"] = href_list[i].text
        ndict["url"] = href_list[i].xpath("./@href")[0]
        ulist.append(ndict)
    # print(ulist)
    return ulist


def download():
    url_list = get_url()
    # for i in range(len(url_list)+1):
    #     url = base_url + url_list[i].xpath("./@href")[0]
    #     title = url_list[i].text
    for i in url_list:
        title = i["name"]
        url = base_url + i["url"]
        # print(title, url, "\n")

        file.write(title)
        file.write("\n")

        print("正在下载：%s....." % title)
        response = requests.get(url, headers=headers)
        context = response.content.decode("gbk")
        # print(type(context))
        html = etree.HTML(context)
        data = html.xpath("//div[@id='content']//p")
        for j in data:
            file.write(j.text)
            file.write("\n")
            # print(j.text, "\n")
    file.close()


if __name__ == '__main__':
    download()
    # get_url()