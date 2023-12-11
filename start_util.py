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
