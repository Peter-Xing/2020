# -*- coding:utf-8 -*-

# python3.6.5

from ShowapiRequest import ShowapiRequest

import json
import urllib.request
import pandas as pd
import os
from openpyxl import Workbook
import numpy as np 
import xlrd
da = xlrd.open_workbook('D:/api/distinct.xlsx')
table = da.sheets()[0]

#87443 records [0 1], 87430 开始.... 到 440
l = []
c = []
for x in range(87000,87443):
	values = []
	row = table.row_values(x)
	l.append(row[0])
	c.append(row[1])
#l 是 list of string,每个string 是classid
#从l[0] 到 l[713]



Da = pd.DataFrame()
CL = []
Drug = []


wb = Workbook()  
ws = wb.active


for x in range(443):
	r = ShowapiRequest("http://route.showapi.com/1468-3","256020","ad6a5ddcfdba4991bb6f020ee0371e9f" )
	r.addBodyPara("classifyId", c[x])
	r.addBodyPara("searchType", "4")
	r.addBodyPara("searchKey", l[x])
	r.addBodyPara("page", "1")
	r.addBodyPara("maxResult", "10")
	res = r.post()
	result = res.json()
	if 'drugList' in result['showapi_res_body']:
		data = pd.DataFrame(result['showapi_res_body']['drugList'])
		Da = Da.append(data)
	else:
		CL.append(c[x])
		Drug.append(l[x])

	print("receiving :        "+str(x))




CC = pd.DataFrame(CL)
DD = pd.DataFrame(Drug)

Da.to_excel('D:/api/medicine.xls')



	
