import socket
import sys
import time

class Connection:
	def __init__(self, local_user_name):
		self.local_user_name = local_user_name
		self.sock = socket.socket()
		self.server_address = ('localhost', 10000)
		print('Trying to connect to {} port {}'.format(self.server_address[0], self.server_address[1]))
		while True:
			try:
				self.sock.connect(self.server_address)
				self.sock.settimeout(2)
				self.sendMessage(self.local_user_name, flag='INIT')
				print('Connection established')
				break
			except ConnectionRefusedError:
				print ('Connection could not be established. Trying again...')
				time.sleep(1)
	def close(self):
		self.sock.close()
		print('Connection closed')
	def sendMessage(self, message, flag=None):
		if flag:
			message = flag+message
			print(message)
			time.sleep(1)
			self.sock.sendall(message.encode())
		else:
			print ('Sending message {}'.format(message))
			time.sleep(1)
			self.sock.sendall(message.encode())
	def readMessage(self):
		while True:
			try:
				data = self.sock.recv(4096).decode()
				if data:
					print(data)
				else:
					break
			except socket.timeout:
                                break 
 



if __name__ == '__main__':
	while True:
		conn = Connection('Kasia')
		time.sleep(1)
		conn.sendMessage('Lukascostamsoctam')
		conn.readMessage()
		conn.close()
