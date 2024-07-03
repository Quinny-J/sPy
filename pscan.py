# I'm still learning python. 
# Made by @Quinny-J
# 03/07/2024

# References 
# Flask - https://flask.palletsprojects.com/en/3.0.x/
# Socket - https://docs.python.org/3/library/socket.html

import socket

# Class is being used to store multiple vars in a catagory in this case strings
class pscan:

    # Port scan function we provide a server address and it will scan 255 ports and check if there open
    def doScan(server_address):
        # Im using a try statement so i can catch the errors without python breaking
        try:
            for port in range(1,255): # Don't want to spam sockets so 255 port s
               sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket
               sock.settimeout(10) # Kill the socket after 10 secs
               result = sock.connect_ex((server_address, port))
            if result == 0:
                    print ("Port {}: Open".format(port))
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
        return "yo"