import json
from socket import socket, AF_INET, SOCK_STREAM
from time import time

from settings import *


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

    def jim_response(self, response_code, alert=None, error=None)
        response_time = int(time())
        response = {"response": response_code, "time": response_time }
        if alert:
            response.update({"alert": alert})
        elif error:
            response.update({"alert": alert})
        return json.loads(response)

    def handle_message(self, address, message):
        print(f'Message: {message.decode("utf-8")} was sent by client from address {address}')


if __name__ == '__main__':
    server = Server()
    server. connect()
    server.run()