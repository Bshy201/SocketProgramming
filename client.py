import socket

#socket object
s = socket.socket()

# The port you want to connect to
port = 10015

# connect to the server on local machine
s.connect(('127.0.0.1', port))

#resv() receives data from the socket
# 1024 bits is the maximun amount of data that can be recived 
# retruns a bytes object that represents the data received
print(s.recv(1024).decode())

s.close()