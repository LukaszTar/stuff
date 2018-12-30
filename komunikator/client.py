import socket
import sys

sock = socket.socket()

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(server_address[0], server_address[1]))

sock.connect(server_address)
sock.settimeout(1)
print(sock.gettimeout())
try:
	message = 'This message will be send back'.encode()
	print ('Sending message {}'.format(message))
	sock.sendall(message)
	while True:
		data = sock.recv(4096).decode()
		print (data)
		if not data: 
			sock.close() 
			break
		print ("received: '{}'".format(data))
except socket.timeout:
	print('closing connection')
finally:
	sock.close()
