"""
安装 pip install beautifulSoup
"""
from bs4 import BeautifulSoup
import re

# 文件路径
file=r'E:\Testcase\build.xml'
# 打开文件
page_file=open(file,encoding='utf-8')
# 读取文件内容
html_handle=page_file.read()
# beautifulSoup解析
soup=BeautifulSoup(html_handle,'html.parser')
# 打印文件头
# print(soup.head)
# 获取文件标签
print(soup.include)
# 获取标签中的属性
print(soup.include.attrs)
# 获取节点的所有选择标签
ps=soup.find_all("include")
print(ps)
# 按css搜索
jobs=soup.find_all("td",class_='')
# <a class='turnto'>小明</a>
name=soup.find_all("a",class_='turnto')

# 正则匹配
r=re.findall(">(.{2,5})</a>",name)