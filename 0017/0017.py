# -*- coding: utf-8 -*-
import xlrd,re,json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


with xlrd.open_workbook('student.xls') as file:
	table = file.sheet_by_index(0) #get sheet's content order by index

rows = table.nrows #行数
cols = table.ncols #列数
dic = {} #dictory

content = '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n<studnets>\n<!--\n    学生信息表\n    "id" : [名字, 数学, 语文, 英语]\n-->\n'

for row in range(rows):
	stu = table.row_values(row) #获取某一行的内容
	list = []
	for x in range(len(stu)-1):
		list.append(stu[x+1])
		# print(isinstance(stu[x+1],unicode)) # 判断是否是unicode编码
	dic[stu[0]] = list

s = json.dumps(dic, indent=4, ensure_ascii=False)

content = content + s + '\n</students>\n</root>'
with open('studnet.xml','w') as f:
	f.write(content)