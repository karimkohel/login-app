############## Imports ###############

from tkinter import *
import backend as bk

############## Inits ###############

lfont = ("Helvetica", 18)
mfont = ("Helvetica", 15)
sfont = ("Helvetica", 12)

############## Fx ###############

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

	lb = Button(root, text='Login', command=login)
	lb.grid(row=3, columnspan=2, pady=10)


def register_page():
	pass

def login():

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
		scs.pack(pady=20)

	else:
		eusername.delete(0,END)
		epassword.delete(0,END)

############## main ###############

root = Tk()
root.geometry("400x250+500+300")

L1 = Label(root, text="Welcome to Login app 2.0", font=lfont)
L1.pack(pady=20)

B1 = Button(root, text='Login', command=login_page, width=10)
B1.pack(pady=20)

B2 = Button(root, text='Register', command=register_page, width=10)
B2.pack(pady=20)


root.mainloop()