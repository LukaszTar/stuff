import socket
import sys
import threading
import time
from tkinter import *
from tkinter import ttk

class Client():
	def __init__(self,username, target_username, server_address = '80.68.239.251', server_port = 10000):
		#sock = socket.socket()
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
				ReceivedMessage(sock).start()
				break
			except ConnectionRefusedError as e:
				print(e,'Trying again...') 
				time.sleep(1)

class ReceivedMessage(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    def run(self):
        while True:
            print('Recieved....')
            data = self.sock.recv(4096)
            if not data: break
            text_chat.config(state='normal')
            text_chat.insert(INSERT, '{}: {}'.format(chat_to_var.get(),data.decode()))
            text_chat.config(state='disabled')
            print('Recived message:',data.decode())
def send():
    sock.sendall(('{}\n'.format(message.get())).encode())
    text_chat.config(state='normal')
    text_chat.insert(END,'{}: {}\n'.format(login_as_var.get(),message.get()))
    text_chat.config(state='disabled')
    message.set('')
def signinWindow():
    root_signin = Toplevel()
    root_signin.title('Sign in')
    frame_signin = Frame(root_signin)
    frame_signin.grid(column=0, row=0, sticky=(N, W, E, S))
    login_as_label = Label(frame_signin, text='Login as')
    login_as_label.grid(column=0, row=0)
    chat_to_label = Label(frame_signin, text='Chat to')
    chat_to_label.grid(column=0, row=1)
    login_as_text = Entry(frame_signin, textvariable=login_as_var, width=12)
    login_as_text.grid(column=1, row=0)
    chat_to_text = Entry(frame_signin, textvariable=chat_to_var, width=12)
    chat_to_text.grid(column=1, row=1)
    sign_button = Button(frame_signin, command=lambda: signin(root_signin), text='Sign in')
    sign_button.grid(column=1, row=3, sticky=(N, E))
    
def signin(root_signin):
    Client(login_as_var.get(), chat_to_var.get())
    remote_username.set('Message to {}'.format(chat_to_var.get()))
    send_message_button.config(state='normal')
    text_input.bind('<Return>', lambda event: send())
    root_signin.destroy()
    pass
sock = socket.socket()

root = Tk()
root.title('Chat')

login_as_var = StringVar()
chat_to_var = StringVar()
remote_username = StringVar()
message = StringVar()
remote_username.set('Message to')
frame = ttk.Frame(root, padding=(5, 5, 12, 0))
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

text_chat = Text(frame, width=50, height = 30, state='disabled')
text_chat.grid(column=0, row=0, sticky=(W))

signin_button = Button(frame, command=signinWindow, text='Sign in')
signin_button.grid(column=0, row=0,sticky=(N,E))

text_input_label = Label(frame, textvariable=remote_username)
text_input_label.grid(column=0, row=1, sticky=(W))

text_input = Entry(frame, width=60, textvariable=message)
text_input.grid(column=0, row=2)

send_message_button = Button(frame, text='Send', command=send, state='disabled')
send_message_button.grid(column=0, row=3, sticky=(N, E))

root.mainloop()
