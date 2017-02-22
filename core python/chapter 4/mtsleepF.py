# -*- coding:utf-8 -*-
from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime


class CleanOutputSet(set):
	def __str__(self):
		return ', '.join(x for x in self)#将默认输出改为以逗号分隔的字符串
lock = Lock()
loops = (randrange(2,5) for x in xrange(randrange(3,7)))
#随机数量的线程(3~6)，每个线程暂停或睡眠(2~4)秒
remaining = CleanOutputSet()

def loop(nsec):
	myname = currentThread().name#保存当前执行它的线程名
	lock.acquire()#获取锁
	remaining.add(myname)
	#线程名添加到remaining集合以及指明启动线程的输出操作时原子的
	#没有其他线程进入临界区
	print '[%s] Started %s' % (ctime(), myname)
	lock.release() #释放锁
	sleep(nsec)    #线程按照预先指定的随机秒数执行睡眠操作
	lock.acquire() #获得锁
	remaining.remove(myname)
	print '[%s] Completed %s (%d secs)' % (ctime(), myname, nsec)
	print '    (remaining: %s)' % (remaining or 'NONE')
	lock.release()

def main():
	for pause in loops:
		Thread(target = loop, args = (pause,)).start()

@register      #使用atexit.register()来注册_atexit()函数
def _atexit(): #以便让解释器在脚本退出前执行该程序
	print 'all DONE at:', ctime()

if __name__ == '__main__':
	main()