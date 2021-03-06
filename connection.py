"""Esablish SSH or TELENT and SERIAL conenction
 using NETMIKO Library AND CONFIGURE THE DEVICE"""
 #Import NETMIKO, TIM,OS AND COLOUR LIBRARIES
from netmiko import (
    ConnectHandler,
    redispatch,
    NetmikoAuthenticationException,
    NetMikoTimeoutException,
)
import time
import csv
import os
from termcolor import colored

#DEFINE THE CLASS CONNECTION
class SINGLE_SSH_TELNET:
    """Function to Connect with the device
    using SSH and TELNET"""

    def __init__(
        self,
        ip,
        username,
        password,
        connection_type,
        config_file,
    ):
        # Argument IP,USERNAME,PASSWORD,CONNECTION TYPE,CONFIG FILE.
        self.ip = ip
        self.username = username
        self.password = password
        self.connection_type = connection_type
        self.config_file = config_file

    def connect(self):
        device = {
            "device_type": self.connection_type,
            "ip": self.ip,
            "username": self.username,
            "password": self.password,
        }

        with open(self.config_file) as f:
            lines = f.read().splitlines()
        print(colored("*" * 100, "green"))
        print(" " * 45 + "Connecting" + device["ip"])
        print(colored("*" * 100, "green"))
        try:
            net_connect = ConnectHandler(**device)
        except NetmikoAuthenticationException:
            print("Entered Credentials are Invalid.")
        except NetMikoTimeoutException:
            print("Cannot connect to this device.")

        output = net_connect.send_config_set(lines)
        print(output)
        print(colored("*" * 100, "green"))
        print(" " * 35 + "Configuration Completed")
        print(colored("*" * 100, "green"))
