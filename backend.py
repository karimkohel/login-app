import sqlite3 as sql
import sys
import hashlib

def user_in_db(usr):

	connection = sql.connect('users.db')

	cursor = connection.cursor()

	cursor.execute("SELECT * FROM users WHERE username=:user",{'user':usr})
	try:
		if usr in cursor.fetchone():
			connection.close()
			return True
	except Exception:
		connection.close()
		return False

def hash_this(pw):

	psw = hashlib.sha512(pw.encode())
	pw_hash = psw.hexdigest()

	return pw_hash 

def pass_in_db(usr,pw):

	connection = sql.connect('users.db')

	cursor = connection.cursor()

	pw_hash = hash_this(pw)
	cursor.execute("SELECT * FROM users WHERE username=:user",{'user':usr})
	try:
		if pw_hash in cursor.fetchone():
			connection.close()
			return True
		else:
			connection.close()
			return False
	except:
		connection.close()
		return False

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

def register(username, pw):
	connection = sql.connect('users.db')
	cursor = connection.cursor()

	pw_hash = hash_this(pw)

	cursor.execute("INSERT INTO users VALUES (:username, :password)",{'username':username, 'password':pw_hash})

	connection.commit()
	connection.close()
