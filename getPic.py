# -*- coding:utf-8 -*-

import requests
import re
import pymysql
import string
# from pyquery import PyQuery as pq
# download pictures from a website


i = 0
for x in range(1,298):
	try:
		html = requests.get('https://www.daquan.com/cyzy/list_'+str(x)+'.html').text
		pic_url = re.findall('target="_blank"><img src="(.*?)" alt=',html,re.S)
		for each in pic_url:
			url = 'https://www.daquan.com/' + each
			print('now downloading:  ' + str(i) + "  in page:  " + str(x))
			pic = requests.get(url)
			fp = open("D:\\图片\\pic" + str(i) + ".jpg","wb")
			fp.write(pic.content)
			fp.close()
			i += 1
	except Exception as e:
		raise e
	
