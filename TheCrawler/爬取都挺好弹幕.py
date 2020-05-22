import requests
import json
from lxml import etree
# from urllib.request import urlretrieve

headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)"}
# f = open(r"D:\pycharm\TheCrawler\弹幕文件\都挺好弹幕.txt", "a", encoding="utf-8")
file = open(r"D:\pycharm\TheCrawler\弹幕文件\都挺好弹幕.json", "a", encoding="utf-8")


def get_end_param():
    param_list=[]
    id_list = get_before_param()
    url = "https://access.video.qq.com/danmu_manage/regist?vappid=97767206&vsecret=c0bdcbae120669fff425d0ef853674614aa659c605a613a4&raw=1"
    for i in id_list:
        data = {"wRegistType": 2, "vecIdList": [i], "wSpeSource": 0, "bIsGetUserCfg": 1,
                "mapExtData": {i: {"strCid": "wu1e7mrffzvibjy", "strLid": ""}}}

        requests.packages.urllib3.disable_warnings()
        response = requests.post(url, json=data, headers=headers, verify=False)

        res = response.json()
        result = res['data']['stMap'][i]['strDanMuKey']
        param_list.append(result.split("=", 4)[-1])
    # print(param_list)
    return param_list


def get_before_param():
    # 获取1-30集的id
    url = "https://v.qq.com/x/cover/wu1e7mrffzvibjy.html"

    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=headers, verify=False)
    res = response.content.decode("utf-8")
    html = etree.HTML(res)
    id_list = html.xpath("//div[@class='mod_episode']//span/@id")
    # print(id_list)
    return id_list

    # 获取31-46集的id
    # url = "https://v.qq.com/x/cover/wu1e7mrffzvibjy/x003061htl5.html"
    # id = url.rsplit("/")[-1]
    # print(id.split(".")[0])


def get_danmu():
    param_list = get_end_param()
    for k in range(len(param_list)):
        # file.write(f"*********************正在爬取第{k+1}集弹幕***********************")
        # file.write("\n")
        # print(f"*********************正在爬取第{k+1}集弹幕***********************", "\n")

        # 获取id
        # print(param_list[k].split('&')[0])
        # print(param_list[k].split('=')[-1])
        for i in range(15, 3000, 30):
            # url = f"https://mfm.video.qq.com/danmu?target_id=3753912718%26vid%3Dt00306i1e62&timestamp={i}"
            url = f"https://mfm.video.qq.com/danmu?target_id={param_list[k].split('&')[0]}%26vid%3D{param_list[k].split('=')[-1]}&timestamp={i}"
            requests.packages.urllib3.disable_warnings()
            response = requests.get(url, headers=headers, verify=False)
            res = eval(response.text)
            # print(res)
            danmu_list = []
            for j in res["comments"]:
                danmu = {}
                # 数据写入txt文件中
                # f.write(j["opername"] + "说：" + j["content"])
                # f.write("\n")
                print(j["opername"] + "说：" + j["content"], "\n")
                # 写入数据到json文件中
                danmu['name'] = j["opername"]
                danmu['danmu'] = j["content"]
                danmu_list.append(danmu)
            file.write(json.dumps(danmu_list, ensure_ascii=False, indent=4)+",\n")
    file.close()


if __name__ == '__main__':
    get_danmu()
    # get_end_param()
    # get_before_param()
