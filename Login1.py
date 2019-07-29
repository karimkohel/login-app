# First attempt to create a login/register system #

            ##### 23 / 7 / 2019 #####

###########################

import sqlite3 as sql
from getpass import getpass
import sys
import hashlib

########## init ##########

connection = sql.connect('users.db')

cursor = connection.cursor()


########## Fx ##########

def greet():
	print("########################################\n     Welcome to the secure app 1.0\n########################################\n")
	print("Do you ?")
	print("1-have an account")
	print("2-need an account")
	print("3-want to exit! (type 3 anywhere in app)")

def user_in_db(usr):
	cursor.execute("SELECT * FROM users WHERE username=:user",{'user':usr}) 
	try:
		if usr in cursor.fetchone():
			return True
	except Exception:
		return False

def hash_this(pw):
	psw = hashlib.sha512(pw.encode())
	pw_hash = psw.hexdigest()
	return pw_hash

def pass_in_db(usr,pw):
	pw_hash = hash_this(pw)
	cursor.execute("SELECT * FROM users WHERE username=:user",{'user':usr})
	if pw_hash in cursor.fetchone():
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
	print("Logged in succesfully !!")

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
			if password_is_easy(username,password1) or len(password1) < 8:
				raise AttributeError

			pw_hash = hash_this(password1)

			cursor.execute("INSERT INTO users VALUES (:username, :password)",{'username':username, 'password':pw_hash})

		except LookupError:
			print("User already exists,try a different username.")

		except ValueError:
			print("Passwords do not match, try again.")

		except AttributeError:
			print("Password is too short or too easy\n -- passwords should be --\n-8 characters or more\n-not too common\n-not same as username")

		else:
			print(f"registerd with username: {username} succesfully !! ")
			break

def password_is_easy(usr,pw):

	easy_passes = [
		'12345678',
		'123456789',
		'1234567890',
		'testing',
		'Testing',
		'password',
		'password1'
	]


	if pw in easy_passes:
		return True
	elif pw == usr:
		return True
	else:
		return False

########## Main ##########

if __name__=="__main__":

	greet()

	num = get_num()

	if num == 1:
		login()
		
	elif num == 2:
		register()

	elif num == 3:
		sys.exit()


	connection.commit()
	connection.close()

