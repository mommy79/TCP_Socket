class Message:

    def ACK(self):
        message = "ACK"
        send_data = self.encode(message)
        return send_data

    def encode(self, send_msg):
        send_data = bytes(send_msg, 'utf-8')
        return send_data

    def decode(self, recv_data):
        recv_msg = str(recv_data, 'utf-8')
        return recv_msg

    def MSG_CS(self):
        print("[MSG] Connection Success!")

    def MSG_NM(self):
        print("[MSG] No Recevied Message!")

    def ERROR_NUM(self):
        print("[ERROR] Wrong Number!")

    def ERROR_CF(self):
        print("[ERROR] Connection Fail!")