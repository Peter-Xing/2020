# -*- coding:utf-8 -*-

# python3.6.5

# from ShowapiRequest import ShowapiRequest
import operator
import pandas as pd
import os
from openpyxl import Workbook
import numpy as np 
import xlrd
da = xlrd.open_workbook('C:/check1.xlsx')
table = da.sheets()[0]


l = []
c = [] # index 0 to 72777
spec = []
spec2 = []
status = [] # match or not 1 
for x in range(1, 72779):  #1 to 72779
	values = []
	row = table.row_values(x)
	l.append(row[1])
	c.append(row[2])
	spec.append(row[1])
	spec2.append(row[2])
	status.append(row[4])

Da = pd.DataFrame()



wb = Workbook()  
ws = wb.active


for y in range(len(l)):

	b = l[y].split('*') # a list of string
	for x in range(len(b)):
		if b[x].find(':') != -1:
			break
		if b[x].find('：') != -1:
			break
		if b[x].find('每') != -1:
			break
		# if b[x].find('瓶装') != -1:
		# 	break
		if b[x].find('mg') != -1:
			b[x] = eval(repr(b[x]).replace('mg','xx'))
			np = b[x].find('xx')
			if  np != -1:
				b[x] = b[x][:np]
				b[x] = str(float(b[x])/1000)
		if b[x].find('%') != -1:
			b[x] = eval(repr(b[x]).replace('%','xx'))
			np = b[x].find('xx')
			if  np != -1:
				b[x] = b[x][:np]
		b[x] = eval(repr(b[x]).replace('g','xx'))
		b[x] = eval(repr(b[x]).replace('S','xx'))
		b[x] = eval(repr(b[x]).replace('T','xx'))
		b[x] = eval(repr(b[x]).replace('ml','xx'))
		b[x] = eval(repr(b[x]).replace('s','xx'))
		b[x] = eval(repr(b[x]).replace('D','xx'))
		b[x] = eval(repr(b[x]).replace('cm','xx'))
		b[x] = eval(repr(b[x]).replace('粒','xx'))
		b[x] = eval(repr(b[x]).replace('板','xx'))
		b[x] = eval(repr(b[x]).replace('袋','xx'))
		b[x] = eval(repr(b[x]).replace('剂','xx'))
		b[x] = eval(repr(b[x]).replace('贴','xx'))
		b[x] = eval(repr(b[x]).replace('大','xx'))
		b[x] = eval(repr(b[x]).replace('中','xx'))
		b[x] = eval(repr(b[x]).replace('盒','xx'))
		b[x] = eval(repr(b[x]).replace('小','xx'))
		b[x] = eval(repr(b[x]).replace('片','xx'))
		b[x] = eval(repr(b[x]).replace('版','xx'))
		b[x] = eval(repr(b[x]).replace('块','xx'))
		b[x] = eval(repr(b[x]).replace('瓶','xx'))
		b[x] = eval(repr(b[x]).replace('支','xx'))
		b[x] = eval(repr(b[x]).replace('帖','xx'))
		b[x] = eval(repr(b[x]).replace('枚','xx'))
		b[x] = eval(repr(b[x]).replace('包','xx'))
		b[x] = eval(repr(b[x]).replace('掀','xx'))
		b[x] = eval(repr(b[x]).replace('锭','xx'))
		b[x] = eval(repr(b[x]).replace('丸','xx'))
		b[x] = eval(repr(b[x]).replace('塑','xx'))
		b[x] = eval(repr(b[x]).replace('张','xx'))
		b[x] = eval(repr(b[x]).replace('锨','xx'))
		b[x] = eval(repr(b[x]).replace('管','xx'))
		np = b[x].find('xx')
		if  np != -1:
			b[x] = b[x][:np]
	spec[y] = b	



	a = c[y].split('*') # a list of string
	for x in range(len(a)):
		if a[x].find(':') != -1:
			break
		if a[x].find('：') != -1:
			break	
		if a[x].find('含尿素') != -1:
			break
		if a[x].find('瓶装 10') != -1:
			break
		if a[x].find('盒装 10') != -1:
			break
		if a[x].find('(4') != -1:
			break
		if a[x].find('mg') != -1:	
			a[x] = eval(repr(a[x]).replace('mg','xx'))
			np = a[x].find('xx')
			if  np != -1:
				a[x] = a[x][:np]
				a[x] = str(float(a[x])/1000)
		if a[x].find('%') != -1:	
			a[x] = eval(repr(a[x]).replace('%','xx'))
			np = a[x].find('xx')
			if  np != -1:
				a[x] = a[x][:np]
		a[x] = eval(repr(a[x]).replace('s','xx'))
		a[x] = eval(repr(a[x]).replace('S','xx'))
		a[x] = eval(repr(a[x]).replace('g','xx'))
		a[x] = eval(repr(a[x]).replace('ml','xx'))
		a[x] = eval(repr(a[x]).replace('块','xx'))
		a[x] = eval(repr(a[x]).replace('cm','xx'))
		a[x] = eval(repr(a[x]).replace('粒','xx'))
		a[x] = eval(repr(a[x]).replace('板','xx'))
		a[x] = eval(repr(a[x]).replace('袋','xx'))
		a[x] = eval(repr(a[x]).replace('贴','xx'))
		a[x] = eval(repr(a[x]).replace('版','xx'))
		a[x] = eval(repr(a[x]).replace('管','xx'))
		a[x] = eval(repr(a[x]).replace('帖','xx'))
		a[x] = eval(repr(a[x]).replace('小','xx'))
		a[x] = eval(repr(a[x]).replace('盒','xx'))
		a[x] = eval(repr(a[x]).replace('片','xx'))
		a[x] = eval(repr(a[x]).replace('丸','xx'))
		a[x] = eval(repr(a[x]).replace('瓶','xx'))
		a[x] = eval(repr(a[x]).replace('支','xx'))
		a[x] = eval(repr(a[x]).replace('枚','xx'))
		a[x] = eval(repr(a[x]).replace('掀','xx'))
		a[x] = eval(repr(a[x]).replace('包','xx'))
		a[x] = eval(repr(a[x]).replace('锭','xx'))
		a[x] = eval(repr(a[x]).replace('塑','xx'))
		a[x] = eval(repr(a[x]).replace('张','xx'))
		a[x] = eval(repr(a[x]).replace('锨','xx'))
		npos = a[x].find('xx')
		if  npos != -1:
			a[x] = a[x][:npos]
	spec2[y] = a	




for x in range(len(spec2)): # spec[0] 对应 excel里第2行
	# exact match numbers
	# spec[x] is a list of strings
	if operator.eq(spec[x],spec2[x]):
		status[x] = 1

for x in range(len(spec2)): # spec[0] 对应 excel里第2行
	# exact match numbers
	# spec[x] is a list of strings
	if operator.eq(spec[x][0],spec2[x][0]): #first number same
		#compare the total of rest
		total1 = 1
		total2 = 1

		for l in range(1,len(spec[x])):
			if spec[x][0].find(':') != -1:
				break
			total1 = total1 * float(spec[x][l])
		for l in range(1,len(spec2[x])):
			if spec2[x][0].find(':') != -1:
				break
			total2 = total2 * float(spec2[x][l])	
		if total1 == total2:
			status[x] = 1

	print("executing  "+str(x)+"   out of   "+str(len(spec2)))


CC = pd.DataFrame(spec)
DD = pd.DataFrame(spec2)
Da = pd.DataFrame(status)

# exact same numer; same total number and first number; changed number from mg to g 
Da.to_excel('c:/STATUS.xlsx')
