# Creado por ale.tryhard
# NinjaHack Toolkit

import os
import sys
import time
import webbrowser as ninja

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
        
os.system("clear")
print(CYAN+"""
     ╔═══════════╗ 
   ╔═╝███████████╚═╗
╔╝███████████████╚╗ 
║█████████████████║ 
║█████████████████║ 
║█████████████████║
║█╔█████████████╗█║ 
╚╦╝███▒▒███▒▒███╚╦╝ 
╔╝██▒▒▒▒███▒▒▒▒██╚╗ 
║██▒▒▒▒▒███▒▒▒▒▒██║ 
║██▒▒▒▒█████▒▒▒▒██║ 
╚╗███████████████╔╝
╔═╬══╦╝██▒█▒██╚╦══╝.▒.. 
║█║══║█████████║　...▒.  
║█║══║█║██║██║█║　.▒..
║█║══╚═╩══╩╦═╩═╩═╦╗▒.  
╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
╔╝█████║█║██║██║█║
║██████║█████████║""")
print()
print(GREEN+"""
===========================
||       NINJA HACK      ||
===========================""")
print()
print()
print(GREEN+"[1] IP-NINJA")
print()
print(GREEN+"[2] DDOS Y DOS TOOLS")
print()
print(GREEN+"[3] INFO GATHERING")
print()
print(GREEN+"[4] HERRAMIENTAS DE CARDING EN GITHUB")
print()
print(GREEN+"[5] SEGUNDO SCANER DE IP")
print()
print(GREEN+"[6] BANEAR WHATSAPP (SOLO COLOMBIA, MEXICO Y VENEZUELA")
print()
opciones = input(RED+"=> ")

if "1" in opciones:
    print()
    slowprint(GREEN+"[!] Iniciando")
    time.sleep(2)
    os.system("cd TOOLS && cd IP-TOOLS && bash ip-ninja-hack")


elif "2" in opciones:
    slowprint(GREEN+"Iniciando...")
    time.sleep(2)
    os.system("cd TOOLS && cd DDOS-DOS && bash hammer.sh")


elif "3" in opciones:
    os.system("cd TOOLS && cd INFORMACION && python2 info.py")

    
elif "4" in opciones:
    print(YELLOW+"""El usuario es
REALHACKRH

y la contraseña es

593""")
    time.sleep(10)
    os.system("cd TOOLS/CARDING && bash carding.sh")

elif "5" in opciones:
    os.system("cd TOOLS && cd IP-TOOLS && bash ninja-scanner.sh")


elif "6" in opciones:
    os.system("git clone https://github.com/BR4Y4N46/WHATSAPP-BANEO && cd WHATSAPP-BANEO")
    os.system("clear")
    print(GREEN+"[1] BANEAR NUMEROS DE MEXICO")
    print(GREEN+"[2] BANEAR NUMEROS DE COLOMBIA")
    print(GREEN+"[3] BANEAR NUMEROS DE VENEZUELA")
    print()
    banearnum = input(WHITE+"=> ")

    if "1" in banearnum:
        os.system("bash BANEOMEXICO.sh")

    elif "2" in banearnum:
        os.system("bash BANEOCOLOMBIA.sh")

    elif "3" in banearnum:
        os.system("bash BANEOVENEZUELA.sh")

    else:
        print(RED+"Opcion invalida :(")

else:
    print(RED+"Opcion Invalida :(")
    time.sleep(1)
    ninja.open("tiktok.com/@ale.tryhard")
    time.sleep(1)
    os.system("python3 ninja.py")
