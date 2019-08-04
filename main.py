############## Imports ###############

from tkinter import *
import backend as bk
import tkinter.messagebox as msg
import os


############## Inits ###############

lfont = ("Helvetica", 18)
mfont = ("Helvetica", 15)
sfont = ("Helvetica", 12)

############## Fx ###############

def exit():
	if msg.askokcancel("Quit", "You want to quit now? *sniff*"):
		root.destroy()

def restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)

def how_to():
	msg.showinfo('isn\'t it simple?',
		'if you have an account login with your credentials, if you don\'t just register'
		)

def about_us():
	msg.showinfo('Info',
		'This is the work of Karim Kohel.\nstarted on the 2nd of june 2019 and finished after 3 months of procrastination on the 5th of july 2019\nfind me @karimkohel on instagram, or github for this project\'s repository\n\n  copyright © KarimKohel\n'
		)

def fail(scenario):
	if scenario == 0:
		msg.showerror('Error', 'enter username and password')
	elif scenario == 1:
		msg.showerror('Error', 'incorrect username or password')
	elif scenario == 2:
		msg.showerror('Error', 'username already exists')
	elif scenario == 3:
		msg.showerror('Error', "Password is too short or too easy\n -- passwords should be --\n-8 characters or more\n-not too common\n-not same as username")

def login_page():
	global llogin, luser, eusername, epassword, lpass, lb

	L1.destroy()
	B1.destroy()
	B2.destroy()

	llogin = Label(root, text='Login', font=mfont)
	llogin.grid(row=0, column=0, columnspan=2, pady=20)

	luser = Label(root, text='Username :', font=sfont)
	luser.grid(row=1, column=0, padx=15, pady=10)

	eusername = Entry(root, width=30, borderwidth=3)
	eusername.grid(row=1, column=1, padx=15, pady=10)

	lpass = Label(root, text='Password :', font=sfont)
	lpass.grid(row=2, column=0, padx=15, pady=10)

	epassword = Entry(root, width=30, borderwidth=3, show='*')
	epassword.grid(row=2, column=1, padx=15, pady=10)

	lb = Button(root, text='Login')
	lb.grid(row=3, columnspan=2, pady=10)
	lb.bind("<Button-1>", login)
	root.bind("<Return>", login)

def register_page():
	global lregister, luser, eusername, epassword, lpass, lb

	L1.destroy()
	B1.destroy()
	B2.destroy()

	lregister = Label(root, text='Register', font=mfont)
	lregister.grid(row=0, column=0, columnspan=2, pady=20)

	luser = Label(root, text='Username :', font=sfont)
	luser.grid(row=1, column=0, padx=15, pady=10)

	eusername = Entry(root, width=30, borderwidth=3)
	eusername.grid(row=1, column=1, padx=15, pady=10)

	lpass = Label(root, text='Password :', font=sfont)
	lpass.grid(row=2, column=0, padx=15, pady=10)

	epassword = Entry(root, width=30, borderwidth=3, show='*')
	epassword.grid(row=2, column=1, padx=15, pady=10)

	lb = Button(root, text='Register')
	lb.grid(row=3, columnspan=2, pady=10)
	lb.bind("<Button-1>", register)
	root.bind("<Return>", register)

def login(*args, **kwargs):

	username = eusername.get()
	password = epassword.get()

	if bk.pass_in_db(username, password):

		llogin.destroy()
		luser.destroy()
		eusername.destroy()
		epassword.destroy()
		lpass.destroy()
		lb.destroy()

		scs = Label(root, text='logged in as '+username, font=mfont)
		scs.grid(row=0, column=0, columnspan=2, padx=100, pady=20)

	elif username == '' or password == '':
		eusername.delete(0,END)
		epassword.delete(0,END)
		fail(0)

	else:
		eusername.delete(0,END)
		epassword.delete(0,END)
		fail(1)

def register(*args, **kwargs):
	global lregister, luser, eusername, epassword, lpass, lb

	username = eusername.get()
	password = epassword.get()

	if bk.user_in_db(username):
		eusername.delete(0,END)
		epassword.delete(0,END)
		fail(2)
	elif username == '' or password == '':
		eusername.delete(0,END)
		epassword.delete(0,END)
		fail(0)

	elif bk.password_is_easy(username, password):
		epassword.delete(0,END)
		fail(3)
	else:
		bk.register(username, password)

		lregister.destroy()
		luser.destroy()
		eusername.destroy()
		epassword.destroy()
		lpass.destroy()
		lb.destroy()

		scs = Label(root, text='Registered as '+username, font=mfont)
		scs.grid(row=0, column=0, columnspan=2, padx=100, pady=20)



############## main ###############
# main config
root = Tk()
root.title("Login app")
root.geometry("400x250+500+300")
if os.name == 'nt':
	root.iconbitmap(root, default='ico.ico')

# menubar creation
menubar = Menu(root)
root.config(menu=menubar)

# filemenu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=restart)
filemenu.add_command(label='Exit', command=exit)


# helpmenu
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='User guide', command=how_to)
helpmenu.add_command(label='About', command=about_us)


# main page components
L1 = Label(root, text="Welcome to Login app 2.0", font=lfont)
L1.grid(row=0, column=0, pady=20, padx=60)

B1 = Button(root, text='Login', command=login_page, width=10)
B1.grid(row=1, column=0, pady=20, padx=60)

B2 = Button(root, text='Register', command=register_page, width=10)
B2.grid(row=2, column=0, pady=20, padx=60)


root.mainloop()