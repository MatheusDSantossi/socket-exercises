import socket
import os
import threading
#import thread

clients = set()
clients_lock = threading.Lock()

def listener(client, address):
    print("Conexão aceita do endereço: ", address)

    with clients_lock:
        clients.add(client)

    try:
        while True:
            data = client.recv(1024)
            if not data:
                break

            else:
                print(repr(data))
                with clients_lock:
                    for c in clients:
                        c.sendall(data)

    finally:
        with clients_lock:
            clients.remove(client)
            client.close()


host = socket.gethostbyname("localhost")
port = 10016

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(3)
th = []


while True:
    print("Servidor está recebendo conexões!")
    client, address = s.accept()
    # th.append(Thread(target=listener, args = (client, address)).start())


s.close()
        
   
