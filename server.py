import socket
import sys
import threading

class Server():
    def __init__(self, server_address = 'localhost', server_port = 10000):
        self.sock = socket.socket()
        self.sock.bind((server_address, server_port))
        self.sock.listen(10)
    def listenForConnections(self):
        while True:
            print ('Waiting for connection')
            conn, client_address = self.sock.accept()
            Connection(conn, client_address).start()            

class Connection(threading.Thread):
    active_connection = True
    current_user = ''
    target_user = ''
    def __init__(self, conn, client_address):
        threading.Thread.__init__(self)
        self.conn = conn
        self.client_address = client_address 
        print('Connection from: {}'.format(client_address))
        try:
            if self.conn.recv(4096) == 'INIT':
                print('incoming "INIT" message. Sending WHO')
                self.conn.sendall('WHO')
                data = self.conn.recv(4096)
                self.current_user == data
                print(data)
            else:
                print('incorrect init message. Dropping connection')
                self.conn.close()
                self.active_connection = False
        except socket.error as e:
            print('Socket.error: {}'.format(e))
            self.conn.close()
        
    def run(self):
        if self.active_connection:
            if self.target_user:
                self.readMessage()
            else:
                try:
                    self.conn.sendall('TARGET')
                    data = self.conn.recv(4096)
                    if data: 
                        self.target_user == data
                        self.conn.sendall('READY')
                        self.readMessage()
                    else:
                        self.conn.close()
                except socket.error as e:
                    print('Socket.error: {}'.format(e))
                    self.conn.close()

    def readMessage(self):
        try:
            while True:
                data = self.conn.recv(4096)
                if not data: break
                print(data)
        finally:
            self.conn.close()


S = Server()
S.listenForConnections()
            
