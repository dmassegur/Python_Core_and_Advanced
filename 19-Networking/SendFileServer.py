import socket


## Create a server to client connection
## Goes with SendFileClient.py!!!
host = 'localhost'
port = 6767

# Socket creation:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # parameters to pass: 1- version of IP: AF_Inet is internet protocol 4, 2- type of connection, sock_stream is tcpip

# once the bracket is created, we need to comunicate between host and port
s.bind((host,port)) 

print('Server listening on port:', port)

s.listen(1) # number of connections the server will open. in this case only 1 client

# The client has to accept that we want to connect to them
c,addr = s.accept()  # accept the connection
# c establishes the connection, it also returns the address of the connection

# receive info from the client
file = c.recv(1024)    # 1024 bytes of info

# read the file sent by the client
try :
    f = open(file,'rb')  # open the file sent by the client in binary!!!
    content = f.read()   # read the file sent by the client
    c.send(content)  # we send the content of the file back to the client
    f.close()   # close the file!!!!
    
except FileNotFoundError :
    print('File not found.')
    # send error back to the client:
    c.send(b'File not found.')    
    
    
c.close()