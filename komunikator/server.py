import socket
import sys
import threading
import time

messages = {}
active_users = []

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
			print(messages, active_users)
			threadLock.acquire()			
			for user in messages:
				if self.current_user in messages[user]:
					for message in messages[user][self.current_user]:
						print('Sendind message from {} to {}'.format(user, self.current_user))
						self.conn.sendall((message).encode())
					messages[user][self.current_user]=[]
			threadLock.release()
			time.sleep(1)

class Connection(threading.Thread):
	active_connection = True
	current_user = ''
	target_user = ''
	def __init__(self, conn, client_address):
		global messages, active_users
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
				threadLock.acquire()
				if self.current_user not in messages: messages[data] = {}
				if self.current_user not in active_users: active_users.append(self.current_user)
				threadLock.release()
				print(data)
			else:
				print('incorrect init message. Dropping connection')
				self.conn.close()
				self.active_connection = False
		except socket.error as e:
			print('Socket.error: {}'.format(e))
			self.conn.close()
        
	def run(self):
		global messages, active_users
		if self.active_connection:
			if self.target_user:
				self.readMessage()
			else:
				try:
					self.conn.sendall('TARGET'.encode())
					data = self.conn.recv(4096).decode()
					if data: 
						self.target_user = data
						threadLock.acquire()
						if self.target_user not in messages[self.current_user]:
							messages[self.current_user][self.target_user] = []
						threadLock.release()
						self.conn.sendall('READY'.encode())
						Message(self.conn, self.current_user).start()
						self.readMessage()
					else:
						print('Closing connection')
						self.conn.close()
				except socket.error as e:
					print('Socket.error: {}'.format(e))
					active_users.remove(self.current_user)
					self.conn.close()

	def readMessage(self):
		global messages, current_user
		try:
			while True:
				data = self.conn.recv(4096).decode()
				if not data: break
				threadLock.acquire()
				messages[self.current_user][self.target_user].append(data)
				threadLock.release()
				print(data)
				
		except socket.error as e:
			print(e)
		finally:
			active_users.remove(self.current_user)
			self.conn.close()

threadLock = threading.Lock()
S = Server()
S.listenForConnections()
            
