import os
import random
import requests

def req():
	os.system("sudo apt update")
	os.system("sudo apt upgrage")
	os.system("sudo apt-get update")

	os.system("sudo apt-get dist-upgrade")


	os.system("pip install random2")
	
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

	os.system("sudo apt autoremove")

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

def nikto():
	global site 
	os.system("clear")
	print("WEB   Scan site   Nikto")
	print("")
	print(f"Target: {site}")
	print("")
	print(" Select from menu:")
	print("")
	print("   1) Fast scan")
	print("   2) Full scan")
	print("   3) Exit")
	print("")
	choice = input("PENCRYSTEG> ")
	try:
		choice = int(choice)
		if choice >= 1 and choice <= 3 :
			pass
		else:
			raise "Error"
	except:
		os.system("clear")
		nmap_web_scan()

	if choice == 1:
		os.system(f"gnome-terminal -e 'bash -c \"nikto -h '{site}'; exec bash\"'")
		os.system("clear")
	elif choice == 2:
		os.system(f"gnome-terminal -e 'bash -c \"nikto -h '{site}' -C all; exec bash\"'")
		os.system("clear")
	elif choice == 3:
		scanners()


def burpsuite():
	os.system(f"gnome-terminal -e 'bash -c \"burpsuite; exec bash\"'")
	os.system("clear")

def nmap_web_scan():
	global site 
	os.system("clear")
	print("WEB   Scan site   Nmap")
	print("")
	print(f"Target: {site}")
	print("")
	print(" Select from menu:")
	print("")
	print("   1) Scan ports")
	print("   2) Scan vulnerabilities")
	print("   3) Scan all ports")
	print("   5) Exit")
	print("")
	choice = input("PENCRYSTEG> ")
	try:
		choice = int(choice)
		if choice >= 1 and choice <= 5 :
			pass
		else:
			raise "Error"
	except:
		os.system("clear")
		nmap_web_scan()
	if choice == 1:
		if site[:7] == "http://":
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site[7:]}; exec bash\"'")
		elif site[:8] == "https://":
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site[8:]}; exec bash\"'")
		else:
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site}; exec bash\"'")
		nmap_web_scan()
	elif choice == 2:
		os.system(f"gnome-terminal -e 'bash -c \"nmap --script vuln {site}; exec bash\"'")
		os.system("clear")
	elif choice == 3:
		if site[:7] == "http://":
			os.system(f"gnome-terminal -e 'bash -c \"nmap -p- {site[7:]}; exec bash\"'")
		elif site[:8] == "https://":
			os.system(f"gnome-terminal -e 'bash -c \"nmap -p- {site[8:]}; exec bash\"'")
		else:
			os.system(f"gnome-terminal -e 'bash -c \"nmap -p- {site}; exec bash\"'")
		os.system("clear")
	elif choice == 4:
		pass
	elif choice == 5:
		scanners()
def fast_scan():
	global site
	# fast or default scan nmap
	if site[:7] == "http://":
		print(site[:7].split(':'))
		if site[len(site)-1] == "/":
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site[7:-1]}; exec bash\"'")
		else:
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site[7:]}; exec bash\"'")
	elif site[:8] == "https://":
		if site[len(site)-1] == "/":
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site[8:-1]}; exec bash\"'")
		else:
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site[8:]}; exec bash\"'")
	else:
		if site[len(site)-1] == "/":
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site[:-1]}; exec bash\"'")
		else:
			os.system(f"gnome-terminal -e 'bash -c \"nmap {site}; exec bash\"'")

	#scan vuln
	os.system(f"gnome-terminal -e 'bash -c \"nmap --script vuln {site}; exec bash\"'")

	# start nikto 
	os.system(f"gnome-terminal -e 'bash -c \"nikto -h {site}; exec bash\"'")

	# start dirb 
	if site[len(site)-1] == '/':
		os.system(f"gnome-terminal -e 'bash -c \"dirb '{site}' -f ; exec bash\"'")
	else:
		tmp_site = site+'/'
		os.system(f"gnome-terminal -e 'bash -c \"dirb '{tmp_site}' -f ; exec bash\"'")

	os.system("clear")
	scanners()

def full_scan():
	global site
	if site[:7] == "http://":
		os.system(f"gnome-terminal -e 'bash -c \"nmap {site[7:]}; exec bash\"'")
	elif site[:8] == "https://":
		os.system(f"gnome-terminal -e 'bash -c \"nmap {site[8:]}; exec bash\"'")
	else:
		os.system(f"gnome-terminal -e 'bash -c \"nmap {site}; exec bash\"'")

	#scan vuln
	os.system(f"gnome-terminal -e 'bash -c \"nmap --script vuln {site}; exec bash\"'")

	# scan all ports
	if site[:7] == "http://":
		os.system(f"gnome-terminal -e 'bash -c \"nmap -p- {site[7:]}; exec bash\"'")
	elif site[:8] == "https://":
		os.system(f"gnome-terminal -e 'bash -c \"nmap -p- {site[8:]}; exec bash\"'")
	else:
		os.system(f"gnome-terminal -e 'bash -c \"nmap -p- {site}; exec bash\"'")

	# start nikto
	os.system(f"gnome-terminal -e 'bash -c \"nikto -h {site} -C all; exec bash\"'")

	# start dirb
	if site[len(site)-1] == '/':
		os.system(f"gnome-terminal -e 'bash -c \"dirb '{site}' /usr/share/dirb/wordlists/big.txt -f -t 100; exec bash\"'")
	else:
		tmp_site = site+'/'
		os.system(f"gnome-terminal -e 'bash -c \"dirb '{tmp_site}' -t 100 /usr/share/dirb/wordlists/big.txt -f -t 100; exec bash\"'")

	os.system("clear")
	scanners()

def dirb_web_scan():
	global site
    if site[:8] == "https://" or site[:7] == "http://":
            wordlist = ""
	    os.system("clear")
	    print("WEB   Scan site Dirb")
	    print("")
	    print(f"Target: {site}")
	    print("")
	    print(" Select from menu:")
	    print("")
	    print("   1) Fast scan")
	    print("   2) Full scan")
	    print("   3) Use my wordlist")
	    print("   4) Exit")
	    print("")
	    choice = input("PENCRYSTEG> ")
	    try:
		    choice = int(choice)
		    if choice >= 1 and choice <= 4 :
			    pass
		    else:
			    raise "Error"
	    except:
		    os.system("clear")
		    scanners()
	    if choice == 4:
		    os.system("clear")
		    scanners()
	    elif choice == 1:
		    os.system(f"gnome-terminal -e 'bash -c \"dirb '{site}' -f; exec bash\"'")
		    os.system("clear")
	    elif choice == 2:
		    os.system(f"gnome-terminal -e 'bash -c \"dirb '{site}' /usr/share/dirb/wordlists/big.txt -f; exec bash\"'")
		    os.system("clear")
	    elif choice == 3:
		    os.system("clear")
		    print()
		    wordlist = input("Enter path to wordlist: ")
		    print()	
		    try:
			    open(wordlist)
			    os.system(f"gnome-terminal -e 'bash -c \"dirb {site} {wordlist} -f; exec bash\"'")
			    os.system("clear")
		    except:
			    print()
			    print("Wordlist not found")
			    print()
			    os.system("sleep 3")
			    os.system("clear")
			    scanners()
    else:
        os.system("clear")
        print("Please enter the target so that it starts with http:// or https://")
        print("For example http://target.com")
        os.system("sleep 2")
        os.system("clear")

		


def scanners():
	# Основное меню скана
	global site
	os.system("clear")
	print("WEB   Scan site")
	print("")
	print(f"Target: {site}")
	print("")
	print(" Select from menu:")
	print("")
	print("   1) Fast scan")
	print("   2) Full scan")
	print("   3) Nmap")
	print("   4) Nikto")
	print("   5) Dirb")
	print("   6) Exit")
	print("")
	choice = input("PENCRYSTEG> ")
	try:
		choice = int(choice)
		if choice >= 1 and choice <= 6 :
			pass
		else:
			raise "Error"
	except:
		os.system("clear")
		scanners()
	if choice == 6:
		WEB()
	elif choice == 4:
		nikto()
	elif choice == 3:
		nmap_web_scan()
	elif choice == 5:
		dirb_web_scan()
	elif choice == 1:
		fast_scan()
	elif choice == 2:
		full_scan()

def nmap():
	# Nmap будет 2 заголовка
	#	Script
	#	Tools
	global site 
	print("WEB   Nmap")
	print("")
	print("")
	# Надо доделать
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
