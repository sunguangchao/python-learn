import random

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
