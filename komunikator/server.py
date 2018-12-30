import socket
import sys
import time

messages = {'Kasia':{'Lukas':['jeden']}}
current_user = '' 

def sendWaitingMessage(connection, remote_user_name):
	global messages
	for local_user_name in messages:
		for user in messages[local_user_name]:
			if user == remote_user_name:
				print(messages)
				message_to_send = '\n'.join(messages[local_user_name][remote_user_name])
				connection.sendall('{}:{}'.format(local_user_name,message_to_send).encode())
				messages[local_user_name].pop(remote_user_name)
				break
def saveMessage(message):
	global messages
	if current_user in messages:
		if message[:5] in messages[current_user]:
			messages[current_user][message[:5]].append(message[5:])
		else:
			messages[current_user] = {message[:5]:[message[5:]]}
	else:
		messages[current_user] = {message[:5]:[message[5:]]}

def saveUserName(user_name):
	global current_user 
	current_user = user_name
	

sock = socket.socket()
server_address = ('localhost', 10000)
print ('Starting server on {} port {}'.format(server_address[0], server_address[1]))
while True:
	try:
		sock.bind(server_address)
		break
	except OSError:
		print('Could not bind socket. Trying again...')
		time.sleep(1)
	
sock.listen(1)

while True:
	print ('Waiting for connection...')
	connection, client_address = sock.accept()
	
	try:
		print ('Connection from: {}'.format(client_address))
		while True:
			data = connection.recv(4096).decode()
			print(data)
			if data[:4] == 'INIT':
				saveUserName(data[4:])
				sendWaitingMessage(connection, data[4:])
			elif not data:
				break
			else:
				saveMessage(data)
	finally:
		connection.close()
