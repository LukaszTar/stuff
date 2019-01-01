import socket
import sys
import threading
import time

messages = {}

class Server():
	def __init__(self, server_address = '192.168.1.251', server_port = 10000):
		while True:
			try:
				self.sock = socket.socket()
				self.sock.bind((server_address, server_port))
				self.sock.listen(10)
				break
			except OSError as e:
				print(e)
	def listenForConnections(self):
		while True:
			print ('Waiting for connection')
			conn, client_address = self.sock.accept()
			Connection(conn, client_address).start()
			
class Message(threading.Thread):
	def __init__(self, conn, current_user):
		print('starting message thread for:{}'.format(current_user))
		threading.Thread.__init__(self)
		self.conn = conn
		self.current_user = current_user
	def run(self):
		while True:
			if self.conn.fileno() == -1: break
			print('in message:',messages, self.conn)
			
			for user in messages:
				if self.current_user in messages[user]:
					for message in messages[user][self.current_user]:
						print('Sendind message from {} to {}'.format(user, self.current_user))
						self.conn.sendall((message+'\n').encode())
					messages[user][self.current_user]=[]
			time.sleep(1)

class Connection(threading.Thread):
	active_connection = True
	current_user = ''
	target_user = ''
	def __init__(self, conn, client_address):
		global messages
		threading.Thread.__init__(self)
		self.conn = conn
		self.client_address = client_address 
		print('Connection from: {}'.format(client_address))
		try:
			if self.conn.recv(4096).decode() == 'INIT':
				print('incoming "INIT" message. Sending WHO')
				self.conn.sendall('WHO'.encode())
				data = self.conn.recv(4096).decode()
				self.current_user = data
				if self.current_user not in messages:
					messages[data] = {}
				print(data)
			else:
				print('incorrect init message. Dropping connection')
				self.conn.close()
				self.active_connection = False
		except socket.error as e:
			print('Socket.error: {}'.format(e))
			self.conn.close()
        
	def run(self):
		global messages
		if self.active_connection:
			if self.target_user:
				self.readMessage()
			else:
				try:
					self.conn.sendall('TARGET'.encode())
					data = self.conn.recv(4096).decode()
					if data: 
						self.target_user = data
						print(messages[self.current_user])						
						print(messages, data, self.target_user, self.current_user)
						if self.target_user not in messages[self.current_user]:
							messages[self.current_user][self.target_user] = []
						self.conn.sendall('READY'.encode())
						Message(self.conn, self.current_user).start()
						self.readMessage()
					else:
						print('Closing connection')
						self.conn.close()
				except socket.error as e:
					print('Socket.error: {}'.format(e))
					self.conn.close()

	def readMessage(self):
		global messages
		try:
			while True:
				data = self.conn.recv(4096).decode()
				if not data: break
				messages[self.current_user][self.target_user].append(data)
				print(data)
				
		except socket.error as e:
			print(e)
		finally:
			self.conn.close()


S = Server()
S.listenForConnections()
            
