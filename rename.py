
# -*- coding:utf-8 -*-
import os

# 按照顺序把图片文件名改成适合批量插入数据库的格式
path = 'D:\\图片\\'
filelist = os.listdir(path)        #列举图片
filelist.sort(key=lambda x:int(x[3:-4])) #按照命名顺序排列
print(filelist)
i = 0
for item in filelist:
	total_num_file = len(filelist)       #单个文件夹内图片的总数
	if item.endswith('.jpg'):
		src = os.path.join(os.path.abspath(path), item)           #原图的地址
		dst = os.path.join(os.path.abspath(path), str(i) + '.jpg')        
		try:
			os.rename(src, dst)
			print ('converting %s to %s ...' % (src, dst))
			i += 1
		except:
			continue
print ('total %d to rename & converted %d jpgs' % (total_num_file, i))
