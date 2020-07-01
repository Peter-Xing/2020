#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
import string
from pypinyin import pinyin,lazy_pinyin,Style

conn = pymysql.connect(host='localhost', user='root', passwd="....", db='yiyao',charset='utf8',use_unicode = 1)
cur = conn.cursor()
sp = []
li = []
sq = []

cur.execute("select id,zym from zy order by id")
for r in cur:
    li.append(r[0])
    sp.append(r[1])
    sq.append(r[1])

y = len(sp)

for x in range(y):
    sp[x] = pinyin(sp[x],style=Style.FIRST_LETTER)# list of list of letter string
    s = ''
    for w in range(len(sp[x])):
        s = s + sp[x][w][0]
    sq[x] = s

for x in range(len(li)):
    sq[x] = "update zy set szm = '"+sq[x]+"' where id = "+str(li[x])


for x in range(0,y):
    cur.execute(sq[x])
    print(x)

conn.commit()
cur.close()
conn.close()

