import urllib.request

import chardet

import re

# 打开网页
page=urllib.request.urlopen('http://www.meituba.com/tag/juesemeinv.html')
# 获取网页源代码
htmlCode=page.read()
# print(chardet.detect(htmlCode)) # 查看编码方式

data=htmlCode.decode('utf-8')
# print(data) #打印网页源代码

# pageFile = open('pageCode.txt','wb')#以写的方式打开pageCode.txt

# pageFile.write(htmlCode)#写入

# pageFile.close()#开了记得关
# 正则表达式
reg=r'src="(.+?\.jpg)"'
# 编译一下，运行更快
reg_img=re.compile(reg)
# 进行匹配
imglist=reg_img.findall(data)

x=0
for img in imglist:
    print(img)
    urllib.request.urlretrieve('http://ppic.meituba.com/uploads/160322/8-1603220U50O23.jpg','%s.jpg'%x)
    x+=1
