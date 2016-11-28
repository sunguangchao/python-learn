# -*- coding: utf-8 -*-

import redis

def store_redis(filepath):
	r = redis.StrictRedis(host = 'localhost',post = 6379,db = 0)
	f = open(filepath,'rb')
	for line in f.readlines():
		code = line.strip()
		#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
		r.lpush('code',code)

if __name__ == '__main__':
	store_redis('Activation_code.txt')