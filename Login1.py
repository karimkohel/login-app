# First attempt to create a login/register system #

            ##### 23 / 7 / 2019 #####

###########################

import sqlite3 as sql
from getpass import getpass

########## init ##########

connection = sql.connect('users.db')

cursor = connection.cursor()

########## Fx ##########

def greet():
	print("########################################\n     Welcome to the secure app 0.1\n########################################\n")
	print("Do you ?")
	print("1-have an account")
	print("2-need an account")
	print("3-want to exit!")

def user_in_db(usr):
	cursor.execute("SELECT * FROM users WHERE username=:user",{'user':usr})
	try:
		if usr in cursor.fetchone():
			return True
	except Exception:
		return False

def pass_in_db(usr,pw):
	cursor.execute("SELECT * FROM users WHERE username=:user",{'user':usr})
	if pw in cursor.fetchone():
		return True
	else:
		return False

def get_num():

	while True:
		try:
			num = input("enter number : ")
			num = int(num)
			if num > 3 or num < 1:
				raise ValueError
		except:
			print("Unrecognized character, please try again")
		else:
			return num

def login():
	while True:
		try:
			username = input("Enter Username : ").lower()
			if not user_in_db(username):
				raise LookupError
			password = getpass(prompt=f"Enter Password for {username} : ")
			if not pass_in_db(username,password):
				raise ValueError

		except LookupError:
			print("User not found, try again.")

		except ValueError:
			print("Incorrect password, try again.")

		else:
			break
	print("Logged in with username and password ",username,password)

def register():
	while True:
		try:
			username = input("Create username : ").lower()
			if user_in_db(username):
				raise LookupError

			password1 = getpass(prompt=f"Create password for {username} : ")
			password2 = getpass(prompt=f"Enter same password again : ")

			if not password1 == password2:
				raise ValueError

			cursor.execute("INSERT INTO users VALUES (:username, :password)",{'username':username, 'password':password1})

		except LookupError:
			print("User already exists,try a different username.")

		except ValueError:
			print("Passwords do not match, try again.")

		else:
			print(f"registerd with username: {username} and password : {password1} ")
			break

def exit():
	pass
	#filler

########## Main ##########

if __name__=="__main__":

	greet()

	num = get_num()

	if num == 1:
		login()
		
	elif num == 2:
		register()


	connection.commit()
	connection.close()






"""
To Do:

	finish database integration
	encrypt passwords inside db
	security checks 
	final touches

"""