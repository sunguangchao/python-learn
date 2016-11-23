# -*- coding:utf-8 -*-
import random
#做为 Apple Store App #独立开发者，你要搞限时促销，为你的应用生成激活码
#（或者优惠券），使用 Python 如何生成 200 #个激活码（或者优惠券）？
def create_num(num,long):
	str = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*_+'
	a = []
	for i in range(num):
		b = ''
		for i in range(long):
			b = b + random.choice(str)
		a.append(b)
	for i in range(len(a)):
		print(a[i])

if __name__ == '__main__':
	create_num(200,10)
