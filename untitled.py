os.system(f"gnome-terminal -e 'bash -c \"nikto -h http://ctf.djambek.com -C all; exec bash\"'")
os.system(f"gnome-terminal -e 'bash -c \"nikto -h http://ctf.djambek.com; exec bash\"'")