from socket import *
from select import *

class Client:
    __SERVER_IP = '127.0.0.1'
    __SERVER_PORT = 10005
    __ADDR = (__SERVER_IP, __SERVER_PORT)
    __BUFSIZE = 1024

    def __init__(self):
        try:
            self.clientSocket = socket(AF_INET, SOCK_STREAM)
            self.__client_info = [self.clientSocket]

        except (KeyboardInterrupt, BrokenPipeError):
            self.clientSocket.close()
            exit()

        else:
            self.Connection_Req()

    def Connection_Req(self):
        self.clientSocket.connect(Client.__ADDR)
        while True:
            try:
                read_socket, write_socket, error_socket = select(self.__client_info,[],[],1)

            except (KeyboardInterrupt, BrokenPipeError):
                self.clientSocket.close()
                exit()

            else:
                if read_socket:
                    recv_data = self.clientSocket.recv(Client.__BUFSIZE)
                    if recv_data:
                        recv_msg = self.decode(recv_data)

                        if recv_msg == 'ACK':
                            print("Connection Success!")

    def Login_Req(self):
        print("test")

    def ACK(self):
        message = "ACK"
        send_data = self.encode(message)
        self.clientSocket.send(send_data)

    def encode(self, send_msg):
        send_data = bytes(send_msg, 'utf-8')
        return send_data

    def decode(self, recv_data):
        recv_msg = str(recv_data, 'utf-8')
        return recv_msg


c = Client()

