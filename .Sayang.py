# -*- coding: utf-8
#Terima Kasih Buat Lu Semua NgT0ND
#Aslamulaikumm Mamang 
#Supporter OF Angga,Dapunta,Yayan,Mr.Risky
#https://github.com/Dumai-991/
import itertools
import threading
import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [×] Modul bs4 belum terinstall!...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
from requests import Session
import re, sys
import sys
from os import system
import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
#from modul import *
################
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[0;94m'
#b='\033[0;97m'
i='\033[0;92m'
c='\033[0;96m'
m='\033[0;91m'
u='\033[0;95m'
k='\033[0;93m'
p='\033[0;97m'
h='\033[0;90m'
P = '\x1b[0;97m' # PUTIH
M = '\x1b[0;91m' # MERAH 
H = '\x1b[0;92m' # HIJAU
I = '\x1b[0;92m' # HIJAU
K = '\x1b[0;93m' # KUNING
B = '\x1b[0;94m' # BIRU
U = '\x1b[0;95m' # UNGU
O = '\x1b[0;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
ajg_lu = ([i, c, m, u, k, p, h, q])
w = pilih(ajg_lu)
#'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
	import requests, bs4, sys, os, subprocess, random, time, re, json
	from concurrent.futures import ThreadPoolExecutor as YayanGanteng
	from datetime import datetime
	from time import sleep
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] Module requests not installed yet")
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")
def license():
    global Beli
    Beli="https://wa.me/6283143565470?text=Hallo+Bang+Saya+Mau+Beli+License+"
    try:
        toket = open('LICENSE.json', 'r').read()
    except IOError:
        print (M+' Lisensi Invalid !');time.sleep (1.0)
        os.system('clear')
        os.system('rm -rf LICENSE.json')
        romz()

    if os.path.exists('LICENSE.json'):
        user1()
    else:
        romz()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(1./500)

def logo():
	os.system("clear")
	jalan("\r"+i+"  _____   ____ ______\n"+i+" / ___/  / __//_  __/ "+w+"||"+c+"Terima Kasih Kepada -->> From\n"+i+"/ (_ /  / _/   / /    "+w+"||"+c+"Angga,Yayan,Dapunta,Risky,Ratu Error\n"+i+"\___/  /___/  /_/     "+w+"||"+c+"Github.com/Dumai-991\n"+i+"   __    ____  _____   ____   _  __   ____   ____\n  / /   /  _/ / ___/  / __/  / |/ /  / __/  / __/\n / /__ _/ /  / /__   / _/   /    /  _\ \   / _/  \n/____//___/  \___/  /___/  /_/|_/  /___/  /___/  \n"+c+"Power Of RATU ERROR")
def romz():
    global Beli
    Beli="https://wa.me/6283143565470?text=Hallo+Bang+Saya+Mau+Beli+License+"
    logo()
    #ahuhah()
    #jalan('\n\x1b[1;95m • \x1b[1;96mSucces Lisensi Siap\x1b[1;92m ✓')
    id = uuid.uuid4().hex[:25]
    idg = open('LICENSE.json', 'w')
    idg.write(id)
    idg.close()
    jalan ('\n'+U+' • '+O+'Lisensi'+M+' : '+H+'' + id+' ✓')
    jalan (U+' • '+M+'Lisensi Belum Di konfirmasi ')
    jalan (U+' • '+O+'Chat Admin Untuk Mengkonfirmasi Lisensi\x1b[1;39m')
    jalan (U+" • "+c+"Jika Nama Anda : Yayan,Angga,Dapunta,Ratu Error !!")
    jalan (U+" • "+k+"Langsung Chat Risky Untuk DiKonfirmasih !!")
    raw_input('\n'+U+' • '+O+'Tekan Enter ')
    os.system('am start ' + Beli + id + ' >/dev/null')
    time.sleep(1)
    os.sys.exit()
def user1():
    global Beli
    Beli="https://wa.me/6283143565470?text=Hallo+Bang+Saya+Mau+Beli+License+"
    try:
        j = open('LICENSE.json', 'r').read()
        r = requests.get('https://github.com/Dumai-991/Server/blob/main/aku_mirip_kontol.txt').text.strip() # Jangan Di ganti bro'i nanti error
        if j in r:
            os.system('clear')
            logo()
            print('\n'+U+' •'+H+' Lisensi TERSEDIA ✓');time.sleep(1)
#            os.system("python .dumai_991.py")
	    True
        else:
            os.system('clear')
            logo()
            jalan ('\n'+U+' •'+M+' Lisensi Tidak Tersedia !');time.sleep(1)
            romz()
            jalan (U+' • '+O+'Chat Admin Untuk Mengkonfirmasi Lisensi\x1b[1;39m')
            raw_input('\n'+U+' • '+O+'Tekan Enter ')
	    os.system('am start ' + Beli + j + ' >/dev/null')
            os.sys.exit()
    except requests.exceptions.ConnectionError:
    	os.system('clear')
        print (M+' [!] Tidak Ada Koneksi Data\x1b[0;97m')
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'LICENSE.json'])
        romz()



license()
