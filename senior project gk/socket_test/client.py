import socket
import pickle

headerSize = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 6379)) #change ip to wherever the server.py is hosted from socket.gethostname()
s.connect((192.168.0.123, 6379))

while True:
    full_msg = b'' #b'' because it comes in as bytes
    new_msg = True
    while True:
        msg = s.recv(16) #buffer size in bytes, may need to increase
        if new_msg:
            print(f"new message length: {msg[:headerSize]}")
            msgLen = int(msg[:headerSize])
            new_msg = False
            
        #full_msg += msg.decode("utf-8")
        full_msg += msg#just sending bytes not

        if len(full_msg)-headerSize == msgLen:
            print("full message recieved")
            #print(full_msg[headerSize:]) #this shows all the bytes if a pickled item is sent

            d = pickle.loads(full_msg[headerSize:])
            print(d)
            
            new_msg = True
            full_msg = b''
                  
    
print(full_msg)
