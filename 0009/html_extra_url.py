#from:agmcs
import re
with open('1.html','rb') as f:
	data = f.read()

data = data.replace('\r','').replace('\b','').replace('\n','')
find = re.compile(r'href="(.*?)"')
result = find.findall(data)
for x in result:
	print x
# re.compile:
# Compile a regular expression pattern into a regular expression object,
# which can be used for matching using its match() and search() methods