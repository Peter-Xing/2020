# -*- coding:utf-8 -*-

import requests
from requests_toolbelt import MultipartEncoder
import pymysql
import string
import json

conn = pymysql.connect(host='localhost', user='root', passwd="aptx4869PETER", db='yiyao',charset='utf8',use_unicode = 1)
cur = conn.cursor()
li = []
sp = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []


cur.execute("select * from zy where id > 10 order by id")
for r in cur:
	li.append(r[1]) #zym  name
	sp.append(r[3])	#xw  xingzhuang
	c3.append(r[4]) #zzgn gongnengzhuzhi
	c4.append(r[6]) #yfyl yongfayongliang
	c5.append(r[7]) #yj	jinji
	c6.append(r[8]) #xf shuomingshu
	c7.append(r[10]) #szm pinyinjianma
	c8.append(r[9]) #tupian  img


url = "http://api-yiyao.jisogo.com/db/save"
for x in range(len(li)):
	data = MultipartEncoder( fields = {"name":li[x],
		"xingzhuang":sp[x],
		"gongnengzhuzhi":c3[x],
		"yongfayongliang":c4[x],
		"jinji":c5[x],
		"shuomingshu":c6[x],
		"pinyinjianma":c7[x],
		"cate1":"中药",
		"img":c8[x]})
	res = requests.post(url=url,data=data,headers = {'Content-Type':data.content_type})
	print(res.text)

cur.close()
conn.close()

