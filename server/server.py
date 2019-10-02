from socket import socket, AF_INET, SOCK_STREAM

from server.settings import *


class Server:

    def __init__(self, address=DEFAULT_ADDRESS, port=DEFAULT_PORT):
        self.address = address
        self.port = port

    def connect(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.address, self.port))
        self.socket.listen(5)

    def run(self):
        while True:
            client, address = self.socket.accept()
            print(f'Request for connection from {address} ')
            client.send('I see you'.encode('ascii'))
            client.close()

    def send_message(self):
        pass

    def receive_message(self):
        pass

    def handle_message(self, message):
        pass
