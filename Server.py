from socket import *
from select import *
from Login import *

class Server:
    # Server의 HOST와 PORT를 담은 변수
    HOST = '127.0.0.1'
    PORT = 10000
    ADDR = (HOST, PORT)

    # TODO: Server의 정보와 접속중인 Client정보를 담는 변수
    __info_list = []
    __client_info = []

    def __init__(self):
        self.Listening()

    # TODO: Client가 접속요청을 대기하는 메소드
    def Listening(self):
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(Server.ADDR)
        serverSocket.listen(3)

        Server.__info_list.append(serverSocket)
        print(Server.__info_list)

        while True:
            try:
                read_socket, write_socket, error_socket = select(Server.__info_list,[],[],1)

            except KeyboardInterrupt:
                serverSocket.close()
                exit()

            else:
                # if : serverSocket의 변화 감지시(Login클래스 호출), else : clientSocket의 변화 감지시
                for sock in read_socket:
                    if sock == serverSocket:
                        clientSocket, client_info = serverSocket.accept()
                        Server.__info_list.append(clientSocket)
                        Server.__client_info.append(client_info)
                        l = Login()
                    else:
                        continue