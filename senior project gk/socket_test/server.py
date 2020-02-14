import socket
import time
import pickle








headerSize = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6379)) #ip and port
s.listen(5) #number of connections

while True:
    clientsocket, address = s.accept()
    #msg = "Welcome to the server!"

    #could use json instead of pickle to transfer a dictionary but doesn't metter
    d = {1: "hey", 2:"there"}
    msg = pickle.dumps(d)

    
    #msg = f'{len(msg):<{headerSize}}' + msg #regular message
    msg = bytes(f'{len(msg):<{headerSize}}', "utf-8") + msg #pickled item sent
    print("Connection from ", address, " has been established!")
    #clientsocket.send(bytes(msg, "utf-8"))
    clientsocket.send(msg)
    #clientsocket.close()


    '''
    while True: #continuous data stream example
        time.sleep(3)
        msg = f"The time is! {time.time()}"
        msg = f'{len(msg):<{headerSize}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
    '''
