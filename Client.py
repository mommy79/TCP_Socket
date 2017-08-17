from socket import *
from select import *

class Client:
    __HOST = '127.0.0.1'
    __PORT = 10003
    __ADDR = (__HOST, __PORT)
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

    # TODO: 연결요청 메소드
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
                        print(type(recv_msg))
                        if recv_msg == 'ACK':
                            print(recv_msg)
                    else:
                        print("Connection Success!")
                        self.Login_Req()


    # TODO: 로그인요청 메소드
    def Login_Req(self):
        print("test")

    # TODO: Server접속의 성공여부를 알려주는 메소드

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

