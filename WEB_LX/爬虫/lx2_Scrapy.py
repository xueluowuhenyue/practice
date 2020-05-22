"""
安装 pip install Scrapy 框架
"""

import scrapy

html=scrapy.Request("http://stockpage.10jqka.com.cn/600004/company/#detail")
print(html)