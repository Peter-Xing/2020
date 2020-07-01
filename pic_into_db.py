# -*- coding:utf-8 -*-

import pymysql
import sys


conn = pymysql.connect(host='localhost', user='root', passwd="123456", db='yiyao',charset='utf8',use_unicode = 1)
cur = conn.cursor()


sql = []
for x in range(5939):
	sql.append("update zy set tupian = NULL where id ="+str(x))

for x in range(598):
	sql[x] = "update zy set tupian ='"+"D:/图片/"+str(x)+".jpg"+"' where id ="+str(x)

for x in range(5939):
	cur.execute(sql[x])
	print(x)
	conn.commit()

cur.close()
conn.close()

