#coding=utf-8
import pymysql
import string



conn = pymysql.connect(host='localhost', user='root', passwd="....", db='yiyao',charset='utf8',use_unicode = 1)
cur = conn.cursor()
sp = []
li = []
sq = []
#"SELECT * FROM drugs where spec is not NULL order by id limit 379 "
cur.execute("select id,zym from zy order by id")
for r in cur:
	li.append(r[0])
	sp.append(r[1])
	sq.append(r[1])

y = len(sp)
for x in range(y):
	npos = sp[x].find('：')
	# 去掉括号后面的内容
	if  npos != -1:
		sp[x] = sp[x][npos+1:]


for x in range(0,y):
	sq[x] = "update zy set zym = '"+sp[x]+"' where id = "+str(li[x])

#for x in range(y):
#	print(sq[x])


for x in range(0,y):
	cur.execute(sq[x])
	print(sp[x])

conn.commit()





cur.close()
conn.close()

