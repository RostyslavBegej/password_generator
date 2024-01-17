import random
import time

print("--- BR Password Generator ---")
print("")

sml = str(input("Your password must contain lowercase letters(y/n): "))
if sml == "y":

	bgl = str(input("Your password must contain uppercase letters(y/n): "))
	if bgl == "y":

		num = str(input("Your password must contain numbers(y/n): "))
		if num == "y":

			sumv = str(input("Your password must contain characters(y/n): "))
			if sumv == "y":

				a = ("abcdefghijklmnopqrstuvwxyz")
				b = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
				c = ("0123456789")
				d = ("!@#$%^&*()_+-=[]|:;<>,.?/")

				allth = a + b + c + d

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()

		elif num == "n":
			sumv = str(input("Your password must contain characters(y/n): "))
			if sumv == "y":

				a = ("abcdefghijklmnopqrstuvwxyz")
				b = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
				d = ("!@#$%^&*()_+-=[]|:;<>,.?/")

				allth = a + b + d

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()
			elif sumv == "n":

				a = ("abcdefghijklmnopqrstuvwxyz")
				b = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

				allth = a + b

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()

	elif bgl == "n":
		num = str(input("Your password must contain numbers(y/n): "))
		if num == "y":

			sumv = str(input("Your password must contain characters(y/n): "))
			if sumv == "y":
				a = ("abcdefghijklmnopqrstuvwxyz")
				c = ("0123456789")
				d = ("!@#$%^&*()_+-=[]|:;<>,.?/")

				allth = a + c + d

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()
			elif sumv == "n":
				a = ("abcdefghijklmnopqrstuvwxyz")
				c = ("0123456789")

				allth = a + c 

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()				
		elif num == "n":
			sumv = str(input("Your password must contain characters(y/n): "))
			if sumv == "y":

				a = ("abcdefghijklmnopqrstuvwxyz")
				d = ("!@#$%^&*()_+-=[]|:;<>,.?/")

				allth = a + d

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()
			elif sumv == "n":

				a = ("abcdefghijklmnopqrstuvwxyz")

				allth = a

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()

elif sml == "n":

	bgl = str(input("Your password must contain uppercase letters(y/n): "))
	if bgl == "y":

		num = str(input("Your password must contain numbers(y/n): "))
		if num == "y":

			sumv = str(input("Your password must contain characters(y/n): "))
			if sumv == "y":

				b = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
				c = ("0123456789")
				d = ("!@#$%^&*()_+-=[]|:;<>,.?/")

				allth = b + c + d

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()
			elif sumv == "n":
				b = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
				c = ("0123456789")


				allth = b + c 

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()				
		elif num == "n":
			sumv = str(input("Your password must contain characters(y/n): "))
			if sumv == "y":

				b = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
				d = ("!@#$%^&*()_+-=[]|:;<>,.?/")				

				allth = b + d

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()
			elif sumv == "n":

				b = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")			

				allth = b

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()		
	elif bgl == "n":
		num = str(input("Your password must contain numbers(y/n): "))
		if num == "y":

			sumv = str(input("Your password must contain characters(y/n): "))
			if sumv == "y":

				c = ("0123456789")
				d = ("!@#$%^&*()_+-=[]|:;<>,.?/")

				allth = c + d

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()
			elif sumv == "n":

				c = ("0123456789")

				allth = c

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()		
		elif num == "n":
			sumv = str(input("Your password must contain characters(y/n): "))
			if sumv == "y":

				d = ("!@#$%^&*()_+-=[]|:;<>,.?/")

				allth = d

				lendth = int(input("Enter the password length: "))

				password = "".join(random.sample(allth, lendth))

				print("Generating a password...")
				time.sleep(2)

				print("The password is ready, your password is: ",password)
				input()
			elif sumv == "n":
				print("")
				print("Sorry, but I can't create a password for you:(")
				input()