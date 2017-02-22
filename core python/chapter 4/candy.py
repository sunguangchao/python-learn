# -*- coding:utf-8 -*-
from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5;
candytray = BoundedSemaphore(MAX)
#当分配一个单位的资源时，计数器值减1，当一个单位的资源返回资源池时，计数器值加1

def refill():
	lock.acquire()
	print 'Refilling candy...',
	try:
		candytray.release()
	except ValueError:
		print 'full, skipping'
	else:
		print 'OK'
	lock.release()

def buy():
	lock.acquire()
	print 'Buying candy...',
	if candytray.acquire(False):
		print 'OK'
	else:
		print 'empty, skipping'
	lock.release()

def producer(loops):
	for i in xrange(loops):
		refill()
		sleep(randrange(3))

def consumer(loops):
	for i in xrange(loops):
		buy()
		sleep(randrange(3))

def _main():
	print 'starting at:', ctime()
	nloops = randrange(2, 6)
	print 'THE CANDY MACHINE (full with %d bars)!' % MAX
	Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
	Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
	print 'all DONE at:', ctime()

if __name__ == '__main__':
	_main()


# starting at: Tue Feb 14 16:07:21 2017
# THE CANDY MACHINE (full with 5 bars)!
# Buying candy... OK
# Refilling candy... OK
# Buying candy... OK
# Refilling candy... OK
# Buying candy... OK
# Refilling candy... OK
# Buying candy... OK
# Buying candy... OK
# Buying candy... OK
# Buying candy... OK
# Buying candy... OK
# Buying candy... empty, skipping
# all DONE at: Tue Feb 14 16:07:30 2017