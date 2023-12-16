import os
import random
import requests

import platform
import subprocess

from start_util import *

def get_package_manager():
    system_type = platform.system().lower()

    if system_type == "linux":
        # Проверяем наличие утилит APT и Pacman
        apt_exists = subprocess.run(["which", "apt-get"], stdout=subprocess.PIPE).returncode == 0
        pacman_exists = subprocess.run(["which", "pacman"], stdout=subprocess.PIPE).returncode == 0

        if apt_exists:
            return "APT"
        elif pacman_exists:
            return "Pacman"
        else:
            return "Не удалось определить менеджер пакетов"
    else:
        return "Не Linux система"


def install_req_apt():
	os.system("sudo apt update")
	os.system("sudo apt upgrage")
	os.system("sudo apt-get update")
	os.system("sudo apt-get dist-upgrade")

	os.system("sudo apt install git")
	os.system("git clone https://github.com/s0md3v/XSStrike.git")
	os.system("cd XSStrike")
	os.system("pip3 install -r XSStrike/requirements.txt")

	os.system("sudo apt install nikto")
	os.system("sudo apt install nmap")
	os.system("sudo apt install burpsuite")
	os.system("sudo apt install chromium")
	os.system("sudo apt install dirb")
	os.system("sudo apt install openvas")
	os.system("sudo apt-get -y install gem")
	os.system("sudo gem install haiti-hash")
	os.system("sudo apt autoremove")

def install_req_pacman():
	os.system("sudo pacman -Syyu --noconfirm")
	os.system("sudo pacman -S git nikto chromium nmap --noconfirm")

	os.system("git clone https://github.com/s0md3v/XSStrike.git")
	os.system("cd XSStrike")
	os.system("pip install -r XSStrike/requirements.txt")

	os.system("yay -S --noconfirm burpsuite dirb")

def req():
	os.system("pip install pip-custom-platform")
	os.system("pip install random2")
	os.system("pip install subprocess.run")

	if get_package_manager() == "APT":
		install_req_apt()
	elif get_package_manager() == "Pacman":
		install_req_pacman()
	else:
		print("Не удалось определить менеджер пакетов")







def start():
	print(" Select from menu:")
	print("")
	print("   1) WEB")
	print("   2) CRYPTO")
	print("   3) STEGO")
	print("   4) Install the necessary add-ons")
	print("   5) EXIT")
	print("")
	choice = input("PENCRYSTEG> ")
	try:
		choice = int(choice)
		if choice >= 1 and choice <= 5 :
			return choice
		else:
			raise "Error"
	except:
		os.system("clear")

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
	print("   0) Choice target")
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


os.system("clear")
picture = random.randint(1,10)
a = open(f'title/{str(picture)}', 'r').read()
print(a)


print("Welcome to pencrysteg!")
site = None
choice = None
while True:
	if choice == None:
		choice = start()
	if choice == 1:
		choice = None
		WEB()

	elif choice == 2:
		pass
	elif choice == 3:
		pass
	elif choice == 4:
		choice = None
		req()
		os.system("clear")
	elif choice == 5:
		exit()
