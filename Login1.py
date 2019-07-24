# First attempt to create a login/register system #

            ##### 23 / 7 / 2019 #####


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
		if usr in users:
			pas = input("Enter password : ")

	elif num == 2:
		usr = input("create username : ")
		if usr in users:
			print("sorry username taken")

		pass
	elif num == 3:
		break

	else:
		
		pass
