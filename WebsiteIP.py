import socket
import subprocess
import sys
from datetime import datetime

socket.setdefaulttimeout(1) 

hostname = str(input("Website: "))

target = socket.gethostbyname(hostname)

print(target)


print("Scanning Target: " + target) 
print("Scanning started at:" + str(datetime.now())) 

   
try: 
      
    for port in range(1,10): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
          
        
        result = s.connect_ex((target,port)) 
        if result ==0: 
            print("Port {} is open".format(port)) 
        
        else:
            print("Port {} is closed".format(port))
        s.close()
           
except KeyboardIntruppt: 
        print("\n Exitting Program !!!!") 
        sys.exit() 
except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit() 
except socket.error: 
        print("\ Server not responding !!!!") 
        sys.exit() 
