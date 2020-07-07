# -*- coding:utf-8 -*-

import requests
from requests_toolbelt import MultipartEncoder
import pymysql
import string
import re
import os

conn = pymysql.connect(host='localhost', user='root', passwd="..", db='yiyao',charset='utf8',use_unicode = 1)
cur = conn.cursor()
li = []
sp = []


# 选出图片是空的数据的zym和id
cur.execute("select zym,id from zy where tupian = 'NULL' and id > 5874 order by id")
for r in cur:
	li.append(r[0]) #zym 
	sp.append(r[1]) #id


#用这些zym在百度图片上搜
for x in range(len(sp)):
	url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + li[x] + '&ct=201326592&v=flip'
	result = requests.get(url)
	result = result.text
	pic_url = re.findall('"objURL":"(.*?)",', result, re.S)
	try:
		pic=requests.get(pic_url[0], timeout=20)
		print("fetching  "+str(x)+"   " + str(sp[x]))
	except requests.exceptions.ConnectionError:
		print('【错误】当前图片无法下载')
	dir = 'C:\\img\\' + str(sp[x]) + '.jpg'
	fp = open(dir, 'wb')
	fp.write(pic.content)
	fp.close()






cur.close()
conn.close()
