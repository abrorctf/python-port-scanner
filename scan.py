#This is a little project to identify the open ports in network.

import sys
import socket
from datetime import datetime
import threading

def scan_port(target, port):    #writing a port scanning function for multiple using
    
    try:
        open_ports = []
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service  = "Unknown"
            answer = f"the port {port} is open - Service {service}"
            open_ports.append(answer)
            print(answer)
            return open_ports
        s.close()
    
    
    #handling different errors which may occur in the process
    
    except Exception as e:              
        print(f"Some unknown error {e} was happen !")
    except socket.error as e:
        print(f"Error linnked with soccket happening: {e} ")

def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Invalid number of arguments entered")
        print("Example for running a script: python.exe scanner.py <target>")
        print("Try again")
        sys.exit(1)
    
    #converting a hostname to ip address: google.com --> 124.14.35.12 like this :)
    try:
        target_ip = socket.gethostbyname(target)
    
    #handling differrent error cases which can occur
    except socket.gaierror:  #det address info error 
        print(f"Error: Unable to convert a hostname {target} to ip address ")
        sys.exit(1)
    
    #Creating a banner
    print("-" * 50)
    print(f"Scanning a {target_ip}")
    print(f"Date/Time of scanning a {target_ip} -> {datetime.now()}")
    print("-" * 50)

    #Creatign a MENU for user:
    print("""
          MENU for SCANNING:
          1) scann all ports
          2) scann well know ports
        """)
    choice = input("Please enter your choice: ")
    
    start_time = datetime.now()
    if choice == "1":
    #Using a threading for scan simultaniously the number of ports 
        try:
            threads = []
            print("scanning all ports")
            for port in range(1,30000):
                thread = threading.Thread(target=scan_port, args=(target_ip,port))
                threads.append(thread)
                thread.start()

        # waiting for a thread to complete that job
            for thread in threads:
                thread.join()
        except KeyboardInterrupt:
            print("\n Exiting a programm: Keybord is Interrupted")
            sys.exit(0)
        except socket.error as e:
            print(f"Socket error: {e}")
            sys.exit(1)

        try:
            threads = []
            for port in range(30000,60000):
                thread = threading.Thread(target=scan_port, args=(target_ip,port))
                threads.append(thread)
                thread.start()

        # waiting for a thread to complete that job
            for thread in threads:
                thread.join()
        except KeyboardInterrupt:
            print("\n Exiting a programm: Keybord is Interrupted")
            sys.exit(0)
        except socket.error as e:
            print(f"Socket error: {e}")
            sys.exit(1)

        try:
            threads = []
            for port in range(60000,65536):
                thread = threading.Thread(target=scan_port, args=(target_ip,port))
                threads.append(thread)
                thread.start()

        # waiting for a thread to complete that job
            for thread in threads:
                thread.join()
        except KeyboardInterrupt:
            print("\n Exiting a programm: Keybord is Interrupted")
            sys.exit(0)
        except socket.error as e:
            print(f"Socket error: {e}")
            sys.exit(1)
        
        print("\n Scan is Compleated !")

    
    if choice == "2":
        try:
            threads = []
            print("scanning well known ports")
            for port in range(1,1025):
                thread = threading.Thread(target=scan_port, args=(target_ip,port))
                threads.append(thread)
                thread.start()

        # waiting for a thread to complete that job
            for thread in threads:
                thread.join()
        except KeyboardInterrupt:
            print("\n Exiting a programm: Keybord is Interrupted")
            sys.exit(0)
        except socket.error as e:
            print(f"Socket error: {e}")
            sys.exit(1)
        print("\n Scan is Compleated for well-known ports!")

    end_time = datetime.now()
    print(f"\nScan finished in: {end_time - start_time }")


if __name__ == "__main__":
    main()
