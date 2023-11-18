import socket
import threading
import json


class Server(threading.Thread):
    def init(self, host="127.0.0.1", port=8888):
        self.server_socket = socket.socket()


class User:
    def init(self, host="127.0.0.1", port=8888):
        self.client_socket = socket.socket()


if __name__ == "__main__":
    server = Server()
    user = User()
