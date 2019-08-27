import socket

filename = input("Enter file to be sent: ")
f = open(filename, "rb")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #s variable is the TCP/IP socket
#AF-Address Family, AF_INET is for IPv4 and AF_INET6 is for IPv6; PF - Protocol Family; SOCK_STREAM tells that it will be a TCP socket.

s.bind((socket.gethostname(), 1234))    #Binding the socket to a port on the server
s.listen(5) #queue of 5 for multiple connection requests

clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")
clientsocket.send(bytes(filename + "@", "utf-8")) #Sending filename with '@' as end of filename
clientsocket.sendfile(f)      #Sending file contents
clientsocket.send(bytes("MSGend", "utf-8")) #End of File msg
f.close()
clientsocket.close()
