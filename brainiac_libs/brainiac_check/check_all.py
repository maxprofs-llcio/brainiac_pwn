import wget
import nmap
import itertools
import socket
import sys
from datetime import datetime
import os
class Check_all:
    def __init__(self,host,ports,protocolo,timeout,ranger):
        self.host=host
        self.ports=ports
        self.protocolo=protocolo
        self.timeout=timeout
        self.ranger=ranger

    def Check_All(ranger,ports,protocolo,timeout):
        os.system("clear")
        remoteServer = input("Enter a remote host to scan: ")
        remoteServerIP = socket.gethostbyname(remoteServer)

        # Print a nice banner with information on which host we are about to scan
        print("-" * 60)
        print("Please wait, scanning remote host", remoteServerIP)
        print("-" * 60)

        # Check what time the scan started
        t1 = datetime.now()

        # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

        # We also put in some error handling for catching errors

        try:
            for port in range(1, 1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    print("Port {}: 	 Open".format(port))
                    if port == 21:
                        print("darkcode")
                sock.close()

        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            sys.exit()

        # Checking the time again
        t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total = t2 - t1

        # Printing the information to screen
        print('Scanning Completed in: ', total)
