import socket

# creates a socket object
s = socket.socket()
print ("Socket Successfully created")

#Reserve a port on this machine 
port = 10015

#bind() locks a server to a specific IP and port
#Since the ip field is empty the server will listen 
#for requests from other computer on the network
s.bind(('', port))
print("socket binded to %s" %(port))

# put the socket to lisiening mode
# the int 5 specifies teh numbber of unaccepted connections 
#allowed before refusing new connections
s.listen(5)
print ("socket is listening")

#an infinte loop 
while True:

    #Establish connection with the client.
    #accept() accepts a connection
    #returns conn & address
    # conn - new socket object
    # address - address bound to socket on other end 
    c, addr = s.accept()
    print ('Got connection from', addr)

    #send() sends data to the sockect s is connect to
    c.send("Thank you for connecting".encode())

    #Close the connection
    c.close()

    break