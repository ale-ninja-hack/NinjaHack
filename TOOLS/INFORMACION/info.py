from urllib2 import *
from platform import system
import sys
import os
 


os.system("clear")

print("\033[1;37m"+'''
   -----------
 | |  NINJA  | |
   -----------
  
  TOOLKIT BY ALE
  ''') 

print('''              \033[1;33m=> Toolkit Ninja Hack

              \033[1;36m Instagram: @ale.tryhard
              TikTok: @ale.tryhard''')



def menu():
   print("\033[0;31m"+'''
.______________________________________________________________________________________.
|                        |                              |                              |
|   1 > DNS Lookup       |       5 > Port Scanner       |     9 > IP-Locator           |
|   ----------------     |       -----------------      |     ---------------------    |                                                      
|   2 > Whois Lookup     |       6 > Extract Links      |     10 > Zone Transfer       |
|   ----------------     |       -----------------      |     ---------------------    |                                                     
|   3 > GeoIP Lookup     |       7 > HTTP Header        |     11 > Revrse IP Lookup    |
|   ----------------     |       -----------------      |     ----------------------   |                                                      
|   4 > Subnet Lookup    |       8 > Host Finder        |                              |
|   -----------------    |        -----------------     |                              |
|________________________|______________________________|______________________________|
''')



menu()
def ext():
    ex = raw_input ('Continuar/Salir:')
    if ex[0].upper() == 'S' :
           print 'Gracias por usar el script ;)'
           exit()
    else:
           clear()
           print banner
           menu()
           select()

def  select():
  try:
    infoxia = input("\033[33m [+] Seleccione una opcion:  ")
    if infoxia == 2:
      dz = raw_input('\033[96mEscribe la direccion IP : ')
      whois = "http://api.hackertarget.com/whois/?q=" + dz
      dev = urlopen(whois).read()
      print (dev)
      ext()
    
    elif infoxia == 11:
      dz = raw_input('\033[96mEscribe la direccion IP : ')
      revrse = "http://api.hackertarget.com/reverseiplookup/?q=" + dz
      lookup = urlopen(revrse).read()
      print (lookup)
      ext()
    
    elif infoxia == 1:
      dz = raw_input('\033[96mEscribe el dominio :')
      dns = "http://api.hackertarget.com/dnslookup/?q=" + dz
      xyks = urlopen(dns).read()
      print (xyks)
      ext()
    
    elif infoxia == 3:
      dz = raw_input('\033[96mEscribe la direccion IP : ')
      geo = "http://api.hackertarget.com/geoip/?q=" + dz
      ip = urlopen(geo).read()
      print (ip)
      ext()
    
    elif infoxia == 4:
      dz = raw_input('\033[96mEscribe la direccion IP : ')
      sub = "http://api.hackertarget.com/subnetcalc/?q=" + dz
      net = urlopen(sub).read()
      print (net)
      ext()
    
    elif infoxia == 5:
      dz = raw_input('\033[96mEscribe la direccion IP : ')
      port = "http://api.hackertarget.com/nmap/?q=" + dz
      scan = urlopen(port).read()
      print (scan)
      ext()
   
    elif infoxia == 6:
      dz = raw_input('\033[96mEscrib el dominio :  ')
      get = "https://api.hackertarget.com/pagelinks/?q=" + dz
      page = urlopen(get).read()
      print(page)
      ext()
    
    elif infoxia == 7:
      dz = raw_input('\033[96mEscribe el dominio :  ')
      hea = "http://api.hackertarget.com/httpheaders/?q=" + dz
      der =  urlopen(hea).read()
      print (der)
      ext()
    
    elif infoxia == 9:
      dz = raw_input('\033[96mEscribe la direccion IP :  ')
      host = "http://ip-api.com/json/" + dz
      kader = urlopen(host).read()
      print (kader)
      ext()

    elif infoxia == 8:
      dz = raw_input('\033[91mEscribe el dominio :    ')
      host = "http://api.hackertarget.com/hostsearch/?q=" + dz
      finder = urlopen(host).read()
      print (finder)
      ext()

    elif infoxia == 10:
     dz = raw_input('\033[92mEscribe el dominio :   ')
     zon = "http://api.hackertarget.com/zonetransfer/?q=" + dz
     tran = urlopen(zon).read()
     print (tran)
     ext()
    
  
  except(KeyboardInterrupt):
    print "\nSigueme en TikTok: @ale.tryhard"
select()
