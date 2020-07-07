# -*- coding:utf-8 -*-

import requests
from requests_toolbelt import MultipartEncoder
import pymysql
import string
import json
import os

conn = pymysql.connect(host='localhost', user='root', passwd="aptx4869PETER", db='yiyao',charset='utf8',use_unicode = 1)
cur = conn.cursor()
li = []
sp = []



cur.execute("select id from zy order by id")
for r in cur:
	li.append(r[0]) #id 
	sp.append(r[0])

# 根据id , 到文件夹里找有无对应图片
# 有的话再上传, 得到返回的upload里的路径，
# 取出这个路径，更新到本地数据库
# 最后本地数据库上传db/save
for x in range(len(li)):
	if os.path.exists("D:\\images\\"+str(li[x])+".jpg"):
		url = "http://api-yiyao.jisogo.com/assets/upload"
		files = {'file':(str(li[x])+".jpg",open('D:\\images\\'+str(li[x])+'.jpg','rb'),'image/jpeg')} 
		res = requests.post(url=url,files=files)
		
		npos = res.text.find('attachment')
		if  npos != -1:
			r = res.text[npos+13:-3] # r 是upload里的路径string


		sp[x] = "update zy set tupian = '"+r+"' where id = "+str(li[x])
		print(li[x])
	else:
		sp[x] = "update zy set tupian = 'NULL' where id = "+str(li[x])
		print(li[x])

for x in range(len(li)):
	cur.execute(sp[x])



conn.commit()

cur.close()
conn.close()

