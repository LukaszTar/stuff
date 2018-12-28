import socket
import sys

sock = socket.socket()
#socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print ('Starting server on {} port {}'.format(server_address[0], server_address[1]))
sock.bind(server_address)
sock.listen(1)

while True:
    print ('Waiting for connection...')
    connection, client_address = sock.accept()
    try:
        print ('Connection from: {}'.format(client_address))
        while True:
            data = connection.recv(4096)
            print(data)
            if data:
                print('Sendind data back: {}'.format(data)) 
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
