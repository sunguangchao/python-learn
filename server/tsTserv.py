import socket from *
import time from ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.blind(ADDR)
tcpSerSock.listen(5)

while True:
	print"waiting for connection..."
	tcpCliSock, addr = tcpSerSock.accept()
	print'...connected from:',addr

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send('[%s] %s' %(ctime(), data))
	tcpCliSock.close()
tcpSerSock.close()
