"""Configure a Cisco Device Using SSH/TELNET method for
a single device USING  Configuration Template. 
SAVE THE COMMANDS REQUIRED TO CONFIGURE ON CONFIG.TXT FILE"""
# Import the Connection Library created on the same folder
# And getpass for colelcting password
import connection
import getpass
from termcolor import colored

ip_add = input(colored("Enter The Device IP Adress:-", "green"))
user_name = input(colored("Enter The Username:-", "red"))
pass_word = getpass.getpass(colored("Enter the Password:- ", "red"))
Connection_mode = input(colored("Enter the Connection Type(telnet/ssh):-", "green"))
if Connection_mode == "telnet":
    Connection_type = "cisco_ios_telnet"
if Connection_mode == "ssh":
    Connection_type = "cisco_ios"
config_file = "config.txt"
# SINGLE_SSH_TELNET is a class defined in connection library
device_data = connection.SINGLE_SSH_TELNET(
    ip_add, user_name, pass_word, Connection_type, config_file
)
device_data.connect()
