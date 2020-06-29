# -*- coding:utf-8 -*-

# python3.6.5
# 网上爬数据，用requests bs4 re
# python 多线程没用，要用多进程来爬数据multi processing
# 用集群来爬数据, 在各台slave上装好scrapy，那么各台机子就变成了一台有抓取能力的slave，在master上装好Redis和rq用作分布式队列。
# 网上爬下来，pymysql 连接存到mysql里
# 页面1到200多，一个循环，每个页面获取该页面的药材的网址
# 每个网址进去，下载内容
import requests
import re
import pymysql
import string
# from pyquery import PyQuery as pq


# 存储html到本地文件夹
i = 0
for x in range(1,298):
	url = "https://www.daquan.com/cyzy/list_"+str(x)+".html"
	k = {'User-Agent': 'Mozilla/5.0'}    
	try:
		r = requests.get(url, headers= k)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		cont = r.text
		ur = re.findall('"title"><a href="(.*?)" target=',cont,re.S)
		print(cont[:10]+str(x))
		for each in ur:
			urls = 'https://www.daquan.com' + each
			print('now downloading:  page: ' + str(x) + " item: " + str(i))
			p = requests.get(urls, headers=k)
			co = p.text
			f = open("D:\\爬虫\\yc" + str(i) + ".html","wb")
			f.write(p.content)
			f.close()
			i += 1

	except:
		print("爬取失败")