import os
import time
os.system('cls')
print("Locating system files...")
# IF SYSTEM FILES DON'T EXIST THEN DO SOMETHING :)
if not os.path.exists("system_scramble/os.py"):
	print("You are missing 'system_scramble/os.py', This is a VERY vital system file. Please get the file for Sami OS version 0.0.7")
	print("To prevent any bugs or errors, the system will shutdown in 10 seconds")
	time.sleep(10)
	exec(open("CrashMyStuff!").read())
if not os.path.exists("system_scramble/write.py"):
	print("The file 'system_scramble/write.py' Does not exist, it is not vital, but you will be limited in the OS of what you can do.")
	print("The OS will startup in 5 seconds, exit if you want to retrieve any system files first.")
	time.sleep(5)
if not os.path.exists("system_scramble/write2.py"):
	print("The file 'system_scramble/write2.py' Does not exist, it is not vital, but you will be limited in the OS of what you can do.")
	print("The OS will startup in 5 seconds, exit if you want to retrieve any system files first.")
	time.sleep(5)
if not os.path.exists("system_scramble/open.py"):
	print("The file 'system_scramble/open.py' Does not exist, it is not vital, but you will be limited in the OS of what you can do.")
	print("The OS will startup in 5 seconds, exit if you want to retrieve any system files first.")
	time.sleep(5)

print("Type in your username to login:")
usern = input()
username = usern.casefold()

if not os.path.exists('user_reserved/' + username + '/'):
	print("This will create a new account, type one if you want to create, type 2 if you want to cancel.")
	choice = input()
	exec(open("system_scramble/boot2.py").read())
if os.path.exists('user_reserved/' + username + '/'):
	exec(open("system_scramble/bootreg.py").read())