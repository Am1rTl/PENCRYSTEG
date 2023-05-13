import os
import random

class WEB:
	def __init__(self,site):
		self.site = site
	def WEB():
		# Основное меню с функциями для пентеста
		global site
		os.system("clear")
		print("WEB")
		print("")
		print(f"Target: {site}")
		print("")
		print(" Select from menu:")
		print("")
		print("   0) Choice site")
		print("   1) Scan site")
		print("   2) SQL attack")
		print("   3) XSS attack")
		print("   4) Nmap")
		print("   5) BurpSuite")
		print("   6) Exit to menu")
		print("")
		choice = input("PENCRYSTEG> ")
		try:
			choice = int(choice)
			if choice >= 0 and choice <= 6 :
				pass
			else:
				raise "Error"
		except:
			os.system("clear")
			WEB()
		if choice == 6:
			os.system("clear")
		elif (choice == 1 and site == None) or (choice == 2 and site == None) or (choice == 3 and site == None):
			os.system("clear")
			print("You have not selected a target site")
			os.system("sleep 2")
			os.system("clear")
			WEB()
		elif choice == 0:
			os.system("clear")
			print("WEB")
			print("")
			print("Please enter the target")
			print("")
			site = input("PENCRYSTEG> ")
			WEB()
		elif choice == 1:
			scanners()
		elif choice == 4:
			nmap()
		elif choice == 5:
			burpsuite()
