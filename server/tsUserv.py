from socket import *
from time import ctime

HOST = ''
PROT = 21567
BUFSIZ = 1024
ADDR = (HOST, PROT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print'wating for message...'
	data ,addr = udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto('[%s] %s' %(ctime(), data), addr)
	print '...received from and return to:',addr
udpSerSock.close()