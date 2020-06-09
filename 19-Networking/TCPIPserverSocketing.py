import socket


## Create a server to client connection
## Goes with TCPIPclientSocketing.py!!!
host = 'localhost'
port = 4000

# Socket creation:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # parameters to pass: 1- version of IP: AF_Inet is internet protocol 4, 2- type of connection, sock_stream is tcpip

# once the bracket is created, we need to comunicate between host and port
s.bind((host,port)) 

print('Server listening on port:', port)

s.listen(1) # number of connections the server will open. in this case only 1 client

# The client has to accept that we want to connect to them
c,addr = s.accept()  # accept when the server tries to connect
# c establishes the connection, it also returns the address of the connection

print('Connection from:',str(addr))


# And now we can start sending info from host to client:
## It needs to be in binary!!!
c.send(b'Hello, how are you?')
c.send('bye'.encode())  # two different ways to print in binary

c.close()  ## closed connection

# s -> send the connection from the server
# c -> client accepts the connection

