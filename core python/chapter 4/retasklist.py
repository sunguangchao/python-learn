import os
import re

f = os.popen('tasklist /nh', 'r')
for eachLine in f:
	print re.split(r'\s\s+',eachLine.rstrip())
f.close()
