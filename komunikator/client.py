import socket
import sys
import threading
import time

class Client():
	def __init__(self,username, target_username, server_address = '80.68.239.251', server_port = 10000):
		sock = socket.socket()
		server_address = (server_address, server_port)
		print('connecting to {} port {}'.format(server_address[0], server_address[1]))	
		while True:
			try:
				sock.connect(server_address)
				sock.sendall('INIT'.encode())
				sock.recv(4096)
				sock.sendall(username.encode())
				sock.recv(4096)
				sock.sendall(target_username.encode())
				sock.recv(4096)
				SendMessage(sock, target_username).start()
				ReceivedMessage(sock).start()
				break
			except ConnectionRefusedError as e:
				print(e,'Trying again...') 
				time.sleep(1)
class SendMessage(threading.Thread):
	def __init__(self, sock, target_username):
		threading.Thread.__init__(self)
		self.sock = sock
		self.target_username = target_username
	def run(self):
		while True:
			data = input('Wiadomosc do {}'.format(self.target_username))
			self.sock.sendall(data.encode())
class ReceivedMessage(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.sock = sock
	def run(self):
		while True:
			data = self.sock.recv(4096)
			if not data: break
			print('Recived message:',data.decode())

username = input('Login as: ')
target_username = input('Chat to: ')
Client(username, target_username)
