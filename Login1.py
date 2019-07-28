# First attempt to create a login/register system #

            ##### 23 / 7 / 2019 #####

###########################
import sqlite3 as sql

########## Fx ##########

def user_in_db(usrname):
	if usrname in users:
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

########## Main ##########

while __name__=="__main__":

	##### intro #####

	print("########################################\n     Welcome to the secure app 0.1\n########################################\n")
	print("Do you ?")
	print("1-have an account")
	print("2-need an account")
	print("3-want to exit!")

	##### main #####

	num = get_num()

	if num == 1:
		while True:
			try:
				username = input("Enter Username : ").lower()
				# logic for checking username
				password = input(f"Enter Password for {username} : ").lower()
				# logic for checking password

			except LookupError:
				print("User not found, try again")

			else:
				break
		print("done corectly username and password are ",username,password)
















	break