import glob
from collections import Counter
import re

def list_txt():
	return glob.glob("*.txt")
#Return a possibly-empty list of path names that match pathname,
#which must be a string containing a path specification

def wc(filename):
	datalist = []
	with open(filename,'r') as f:  #important
		for line in f:
			content = re.sub("\"|,|\.","",line)          #??
			datalist.extend(content.strip().split(' '))  #??
	return Counter(datalist).most_common(1)

def most_common():
	all_text = list_txt
	for txt in all_text:
		print wc(txt)

if __name__ == '__main__':
	print map(wc,list_txt())
#map(function, iterable, ...) :
#Apply function to every item of iterable and return a list of the results

#Help on function sub in module re:
#sub(pattern, repl, string, count=0, flags=0)
#    Return the string obtained by replacing the leftmost
#    non-overlapping occurrences of the pattern in string by the
#    replacement repl.  repl can be either a string or a callable;
#    if a string, backslash escapes in it are processed.  If it is
#    a callable, it's passed the match object and must return a replacement string to be used.