import socket
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ""
filename = ""
file = True
c = 0
while True:
    msg = s.recv(16).decode("utf-8")   #recieving message with buffer size 16
    if file and '@' in msg:
        for k in msg:
            while k != '@':
                filename += k
                c += 1
                break
            if k == '@':
                break
        file = False
        full_msg += msg[c:]
        continue
    if "MSGend" in msg:
        break
    full_msg += msg

full_msg = full_msg
print(full_msg)
f = open(filename, "w")
f.write(full_msg)
f.close()
