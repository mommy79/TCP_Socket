from socket import *
from select import *
from Login import *

class Server:
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Server의 HOST와 PORT를 담은 변수 
    HOST = '127.0.0.1'
    PORT = 10003
    ADDR = (HOST, PORT)
    BUFFSIZE = 1024

    # TODO: Server의 정보와 접속중인 Client정보를 담는 변수 
    __info_list = []
    __client_info = []

    def __init__(self):
        Server.serverSocket.bind(Server.ADDR)
        Server.serverSocket.listen(3)
        Server.__info_list.append(Server.serverSocket)
        self.Listening()

    # TODO: Client가 접속요청을 대기하는 메소드
    def Listening(self):
        while True:
            try:
                read_socket, write_socket, error_socket = select(Server.__info_list,[],[],1)

            except (KeyboardInterrupt, OSError):
                Server.serverSocket.close()
                exit()

            else:
                for sock in read_socket:
                    if sock == Server.serverSocket:
                        clientSocket, client_info = Server.serverSocket.accept()
                        Server.__info_list.append(clientSocket)
                        Server.__client_info.append(client_info)
                        self.ACK()
                    else:
                        continue

    def ACK(self):
        message = "ACK"
        send_data = self.encode(message)
        Server.__info_list[1].send(send_data)

    def encode(self, send_msg):
        send_data = bytes(send_msg, 'utf-8')
        return send_data

    def decode(self, recv_data):
        recv_msg = str(recv_data, 'utf-8')
        return recv_msg


s = Server()