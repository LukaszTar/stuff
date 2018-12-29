import socket
import sys

sock = socket.socket()

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(server_address[0], server_address[1]))

sock.connect(server_address)
try:
    message = 'This message will be send back'
    print ('Sending message {}'.format(message))
    sock.sendall(message)
    while True:
        data = sock.recv(4096)
        if not data: break
        print ("received: '{}'".format(data))
finally:
    sock.close()
