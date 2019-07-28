# First attempt to create a login/register system #

            ##### 23 / 7 / 2019 #####

########## inits ##########

import sqlite3 as sql


def user_in_db(usrname):
	if usrname in users:
		return True
	else:
		return False










########## Main ##########

while __name__=="__main__":

	##### intro #####

	print("########################################\n     Welcome to the secure app 0.1\n########################################\n")
	print("Do you ?")
	print("1-have an account")
	print("2-need an account")
	print("3-want to exit!")

	##### main #####

	num = input("enter number : ")

	if num == 1:
		print("then by all means please carry on")
		usr = input("Enter username : ").lower()

	elif num == 2:
		usr = input("create username : ")
		while user_in_db(usr):
			print("Sorry username already in use. Try again")
			usr = input("create username : ")

		pass
	elif num == 3:
		break

	else:
		
		pass

