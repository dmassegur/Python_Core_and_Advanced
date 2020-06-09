import socket


## create a tcpip client that will connect to the server on port 4000
## Goes with TCPIPserverSocketing.py!!!
s = socket.socket()  #default type of connection

#connection 
s.connect(('localhost',4000))


# HOw to receive the messages that have been sent by the server from serversocketing.py
msg = s.recv(1024)  # receiving the message for the first time

while msg: # while we keep on receiving messages keep displaying them
    print('Received: ', msg.decode(),'\n')  #to convert from binary to ascii
    msg = s.recv(1024)    # 1024 bytes of info
  
# Close the connection once finished transfer  
s.close()