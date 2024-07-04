# I'm still learning python. 
# Made by @Quinny-J
# 03/07/2024

# References 
# Flask - https://flask.palletsprojects.com/en/3.0.x/
# Socket - https://docs.python.org/3/library/socket.html

import socket
import sys
import util
from concurrent.futures import ProcessPoolExecutor, as_completed

# Class is being used to store multiple vars in a catagory in this case strings
class pscan:

    # Trying to keep it neat
    class port_data:
        open_ports = [] # Put all of our open ports in a list for later
        closed_ports = [] # Put all of our closed ports in a list for later


    # Port scan function we provide a server address and it will scan 255 ports and check if there open
    # This is super slow needs to be improved adnd worked on
    def do_range_scan(server_address):
        # Im using a try statement so i can catch the errors without python breaking
        try:
            for port in range(1,255): # Don't want to spam sockets so 255 ports
               sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket
               sock.settimeout(1) # Kill the socket after 5 secs
               result = sock.connect_ex((server_address, port))
               if result == 0:
                    print (f"Port {port}: {util.statusMsg.OPEN}")
                    pscan.port_data.open_ports.append(f'Port {port}: OPEN')
                    return True
               else:
                    print (f"Port {port}: {util.statusMsg.CLOSED}")
                    pscan.port_data.closed_ports.append(f'Port {port}: CLOSED')
                    return False
            
            sock.close()

        except KeyboardInterrupt:
            print ("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print ('Hostname could not be resolved. Exiting')
            sys.exit()
            
        except socket.error:
            print ("Couldn't connect to server")
            sys.exit()

    # Port scan function we provide a server address and it will scan 255 ports and check if there open
    # This is super slow needs to be improved adnd worked on
    def do_sing_scan(server_address, server_port):
        # Im using a try statement so i can catch the errors without python breaking
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket
            sock.settimeout(1) # Kill the socket after 5 secs
            result = sock.connect_ex((server_address, int(server_port)))
            if result == 0:
                print (f"Port {server_port}: {util.statusMsg.OPEN}")
                return f"Port {server_port}: OPEN"
            else:
                print (f"Port {server_port}: {util.statusMsg.CLOSED}")
                return f"Port {server_port}: CLOSED"
                

        except KeyboardInterrupt:
            print ("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print ('Hostname could not be resolved. Exiting')
            sys.exit()
            
        except socket.error:
            print ("Couldn't connect to server")
            sys.exit()