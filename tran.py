#coding=utf-8
import pymysql
import string



conn = pymysql.connect(host='localhost', user='root', passwd="aptx4869PETER", db='yiyao',charset='utf8',use_unicode = 1)
cur = conn.cursor()
sp = []
li = []
sq = []
#"SELECT * FROM drugs where spec is not NULL order by id limit 379 "
cur.execute("select id,manu from yp where manu like '%国产%' order by id")
for r in cur:
	li.append(r[0])
	sp.append(r[1])
	sq.append(r[1])


#print(type(sp))


#打印

y = len(sp)

#	for w in range(0,z):
#			pass
#		li.append(sp[x][w])#.encode("utf8")

#a = len(li)

#print(li)


for x in range(0,y):
	sp[x] = eval(repr(sp[x]).replace('国产','useless'))
	npos = sp[x].find('useless')
	
	if  npos != -1:
		sp[x] = sp[x][:npos-1]

#for x in range(0,y):
#	print(sp[x])


for x in range(0,y):
	sq[x] = "update yp set manu = '"+sp[x]+"' where id = "+str(li[x])

#for x in range(y):
#	print(sq[x])


for x in range(0,y):
	cur.execute(sq[x])
	print(x)

conn.commit()





cur.close()
conn.close()

