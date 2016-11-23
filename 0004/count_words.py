#-*- coding:utf-8 -*-
import re

def count_words(filepath):
	f = open(filepath,'rb')
	s = f.read()
	words = re.findall(r'[0-9a-zA-Z]+',s)
#	Return all non-overlapping matches of pattern in string, as a list of strings.
	return len(words)

if __name__ == '__main__':
	num = count_words('count_test.txt')
	print num