import urllib.request
import chardet

page = urllib.request.urlopen('http://www.meituba.com/tag/juesemeinv.html') # 打开网页
htmlCode=page.read() # 获取网页源代码

# print(chardet.detect(htmlCode)) #查看编码方式

data=htmlCode.decode('utf-8')

# print(data) # 打印网页源代码
pageFile=open('pageCode.txt','wb')     # 以写的方式打开pageCode.txt

pageFile.write(htmlCode)  # 写入

pageFile.close()          # 开了记得关
