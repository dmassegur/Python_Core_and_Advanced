import socket


## create a tcpip client that will connect to the server on port 4000
## Goes with SendFileClient.py!!!
s = socket.socket() #default type of connection

#connection 
s.connect(('localhost',6767))

fn = input('Enter a file name: ')

# send the file to the server
s.send(fn.encode())  # sent in binary

# receive the content of the file sent by the server
content = s.recv(1024)  # 1024 bytes of info

print(content.decode())  # decode from binary and print the content that server has sent

# Close the connection once finished transfer  
s.close()