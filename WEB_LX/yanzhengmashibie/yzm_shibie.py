from WEB_LX.yanzhengmashibie.ShowapiRequest import ShowapiRequest


def read_yzm(url, typeid, pic_path):
    # 使用接口环境访问接口地址===>前提要注意联网
    jw1 = ShowapiRequest(url, "98774", "d42cb73ba61e4f6a9bc15bf7c55f0d57")
    # 增加接口请求的参数
    jw1.addBodyPara("typeId", typeid)
    jw1.addBodyPara("convert_to_jpg", "0")
    # 告诉接口识别的验证码图片文件
    jw1.addFilePara("image", pic_path)
    # 访问接口
    result = jw1.post().json()
    print(result)
    # 从json提炼出有效的数据
    text = result['showapi_res_body']['Result']
    print("验证码是", text)
    return text


if __name__ == '__main__':
    read_yzm("http://route.showapi.com/184-4", 34,
            r'D:\Pycharm\Scripts\WEB_LX\data\yzm.png')