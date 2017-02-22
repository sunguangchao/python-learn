
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/dp/1602069921'
ISBNs = {
	'0132269937': 'Core python Programning',
	'0132356139': 'Python Web Development with Django',
	'0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
	page = uopen('%s%s' % (AMZN, isbn))
	date = page.read()
	page.close()
	return REGEX.findall(date)[0]

def _showRanking(isbn):
	print '- %r ranked %s' %(ISBNs[isbn], getRanking(isbn))

def main():
	print 'At', ctime(), 'on Amazon...'
	for isbn in ISBNs:
		_showRanking(isbn)

@register
def _atexit():
	print 'all DONE at', ctime()

if __name__ == '__main__':
	main()