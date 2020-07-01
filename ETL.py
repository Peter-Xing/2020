# -*- coding:utf-8 -*-

import re
import pymysql
import string
from bs4 import BeautifulSoup
from w3lib import html
from lxml import etree

conn = pymysql.connect(host='localhost', user='root', passwd="123456", db='yiyao',charset='utf8',use_unicode = 1)
cur = conn.cursor()


#5939
for x in range(5939):
	soup = BeautifulSoup(open('D:\\爬虫\\yc'+str(x)+'.html',encoding='utf-8'),features='html.parser')
	co=soup.find_all(class_='content')
	co = str(co)
	dr = re.compile(r'<[^>]+>',re.S)
	result = dr.sub('',co)
	result = result.replace('\n','')
	result = result.replace('\t','')
	result = result.replace('[','')
	result = result.replace(']','')
	li = result.split('【')#list of string
	# result是一个string
	# print(result)

	# 把result根据标签 '..】'，拆分成多个string,分别插入对应的字段
	# print(li) # [0] 到 [n], 先判断里面是哪个字段的

	# 根据字段创建list of string, 从[0]对应第一个mysql里的字段，没有的就插入'NULL'代替，每insert一次更新一次
	val = [1,1,1,1,1,1,1,1,1]
	val[0] = x #插入id


	# 有中文名标签的按那个string来，没有的看第一个string的长度来判断
	# 异名 或 别名
	n = len(li)
	zwm = 0
	bm = 0
	xw = 0
	zzgn = 0
	gj = 0
	yfyl = 0
	yj = 0
	xf = 0

	if len(li[0]) < 25 and len(li[0]) > 0:
		val[1] = li[0]
		zwm = 1
	for a in range(n):
		
		po2 = li[a].find('中文名】')
		po = li[a].find('别名】')
		pos= li[a].find('异名】')
		po3 = li[a].find('性味】')
		po4 = li[a].find('功用主治】')
		po44=li[a].find('功能主治】')
		po5 = li[a].find('归经】')
		po6 = li[a].find('用法与用量】')
		po7 = li[a].find('宜忌】')
		po8 = li[a].find('选方】')
		
		if po2 != -1 and zwm == 0: # 中药名
			val[1] = li[a][4:]
			zwm = 1
		elif po2 == -1 and zwm == 0:
			val[1] = "NULL"

		if po != -1 or pos != -1: # 异名
			val[2] = li[a][3:]
			bm = 1
		elif po == -1 and pos == -1 and bm == 0:
			val[2] = "NULL"
			bm = 1

		if po3 != -1: # 性味
			val[3]=li[a][3:]
			xw = 1
		elif po3 == -1 and xw == 0:
			val[3]=("NULL")
			xw = 1

		if po4 != -1 or po44 != -1: # 主治功能
			val[4]=(li[a][5:])
			zzgn = 1
		elif po4 == -1 and po44 == -1 and zzgn == 0:
			val[4]=("NULL")
			zzgn = 1

		if po5 != -1: # 归经
			val[5]=(li[a][3:])
			gj = 1
		elif po5 == -1 and gj ==0:
			val[5]=("NULL")
			gj = 1

		if po6 != -1: # 用法与用量
			val[6]=(li[a][6:])
			yfyl = 1
		elif po6 == -1 and yfyl == 0:
			val[6]=("NULL")
			yfyl = 1

		if po7 != -1: # 宜忌
			val[7]=(li[a][3:])
			yj = 1
		elif po7 == -1 and yj == 0:
			val[7]=("NULL")
			yj = 1

		if po8 != -1: # 选方
			val[8]=(li[a][3:])
			xf = 1
		elif po8 == -1 and xf == 0:
			val[8]=("NULL")
			xf = 1

	# print(val)

	# insert into mysql table
	sql = "INSERT INTO zy(id,zym,bm,xw,zzgn,gj,yfyl,yj,xf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	vals = (val)
	cur.execute(sql, vals)
	conn.commit()
	print("inserting  "+ str(x))


cur.close()
conn.close()
