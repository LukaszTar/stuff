from tkinter import *
from tkinter import ttk

def changeName():
	if text_to_display.get() == 'initial value':
		text_to_display.set('target value')
	else:
		text_to_display.set('initial value')

root = Tk()

frame1 = ttk.Frame(root, width=350, height=350, relief='sunken', borderwidth=2).grid()
frame2 = ttk.Frame(root, width=200, height=200, padding=(5,10)).grid()
text_to_display = StringVar()
text_to_display.set('initial value')
label = ttk.Label(frame2, text='Full name:', textvariable=text_to_display, anchor='center').grid()
button = ttk.Button(text='button', command=changeName).grid()

root.mainloop()
