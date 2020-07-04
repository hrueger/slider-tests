#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "0.0.0.0"#socket.gethostname() # Get local machine name
port = 5000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(1)#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "0.0.0.0"#socket.gethostname() # Get local machine name
port = 5000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(1)

someoneConnected = False

someoneConnected = False
while True:
    while someoneConnected:
        data = conn.recv(1024)
        if data:
            data = data.decode("utf-8") 
            #print("no data")
            if data == "DISCONNECT":
                conn.close()
                someoneConnected = False
            print(data)
    print("keiner verbunden!")
    conn, addr = s.accept()
    print('Got connection from', addr)
    someoneConnected = True

