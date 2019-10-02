from socket import socket, AF_INET, SOCK_STREAM

from settings import *


class Client:
    def __init__(self):
        pass

    def connect_to_server(self, address, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((address, port))
        msg = self.socket.recv(1024)
        self.socket.close()
        print(f'Server says: {msg.decode("ascii")}')


if __name__ == '__main__':
    client = Client()
    client.connect_to_server(DEFAULT_ADDRESS, DEFAULT_PORT)
