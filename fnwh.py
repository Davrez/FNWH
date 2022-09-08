#!/usr/bin/python
# response Script
# version : 0.01
# Credits to @VenomNoob (telegram)
#remade by @DavrezSun (telegram)
import os
import time
from termcolor import *
import datetime
now = datetime.datetime.today()
import requests,sys
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry 
#here the terminal clear he he 😁 
os.system('clear')

if not os.path.exists('results'):
   os.makedirs('results')
class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print("")
print("")
print("")
banner ="""
             _____   _   _  __        __  _   _  ™
            |  ___| | \ | | \ \      / / | | | |
            | |_    |  \| |  \ \ /\ / /  | |_| |
            |  _|   | |\  |   \ V  V /   |  _  |
            |_|     |_| \_|    \_/\_/    |_| |_|
    
            Free       Net      World     Hackers
"""
print(banner)
print("")
print("")
print("")
print("""                 ==========================""")
print("""                    Simple Http response
                     code scanner FNWH
                     -Dev (@Davrezsun)
                         
                         V1.0.2
""")
print("""                 ==========================""")
print("")
print("")
print("""                       Please Wait...""")
time.sleep(2)
print("")
print("""                     Starting Scanner""")
time.sleep(1.5)
print(f"""                         {bcolors.OKGREEN}Success!{bcolors.ENDC}""") 
time.sleep(0.5)
# COLORS #
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if (len(sys.argv) != 2):
    print("""\nUSAGE :
             \n  [ $python3 fnwh.py list.txt]""")
    sys.exit()

else:
  f = open(sys.argv[1],'r') 
  lines = f.readlines()
  f.close()

  filename = 'results/' + sys.argv[1].replace('../','') + '_results.txt'
  out = open(filename, 'w+')

  
for line in lines:
    try:
      
      if 'http://' in line.strip() or 'https://' in line.strip():
        url = line.strip()
      else:
        
        url = 'http://' + line.strip()
      
      s = requests.Session()
      
      r = s.head(url, timeout=1.5)
      response = r.headers
  
      out.write(url + ':' + str(r.status_code) + '\n')

    except requests.ConnectionError as e:
      print("\n", bcolors.ENDC + url + bcolors.FAIL + " Can't connect",bcolors.ENDC )
      continue
    except requests.Timeout as e:
        print("\n[!] : Oops Timeout")
        continue
    except requests.RequestException as e:
        print("\n[!] : General Error")
        continue
    
    except KeyboardInterrupt:
      out.close()
      print("\n\n >>> Results saved in : " + filename + '\n')
      exit()
    
    # Printing the results
    if (r.status_code == 200):
    	try:
        	print("\n", '\x1b[6;30;42m' 'OK200 GOOD', bcolors.ENDC, ':' , url,r.headers['server'], bcolors.ENDC )
    	except KeyError:
            print('\n[!] : server not found')
    
    if (r.status_code == 308):
    	try:
    		print("\n", '\x1b[6;39;40m' '[308]',bcolors.OKBLUE, ':' , url,r.headers['server'], bcolors.ENDC)
    	except KeyError:
            print('\n[!] : server not found')
    		    
    if (r.status_code == 302):
        print('\n', '\x1b[6;39;40m' '[302]',bcolors.OKGREEN, ' : ' , url,r.headers['server'],  bcolors.ENDC)

    if (r.status_code == 301):
    	try:
    		print("\n", '\x1b[6;39;40m' '[301]',bcolors.OKGREEN, ':' , url,r.headers['server'], bcolors.ENDC)
    	except KeyError:
            print('\n[!] : server not found')
    
    if (r.status_code == 403):
    	try:
    		print("\n", '\x1b[6;39;40m' '[403]',bcolors.OKGREEN, ':' , url,r.headers['server'], bcolors.ENDC)
    	except KeyError:
            print('\n[!] : server not found')
print("")
print("")
print(f"""                       {bcolors.OKGREEN}[Done!]{bcolors.ENDC}""")
print("")
print("")
print("=====================================================")
print("\n Your Results are saved in : " + filename + '\n')
print("=====================================================")
print("")
print("")
out.close()


