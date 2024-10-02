import socket 
import sys

try:
    #creates an empty socket 
    #AF_INET = IPv4 adress | use AF_INT6 for IPv6
    #SOCK_STREAM = TCP 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))

#port 80 is the default port used for HTTP
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    #If the host name can't be resolved to an IP address
    print("there was an error resolving the host")
    sys.exit()

#Connecting to host_ip's server
s.connect((host_ip, port))

print("The socket has successfully connected to google")