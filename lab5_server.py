import socket
import threading
import time


class ConnectClient(threading.Thread):
    def __init__(self, client_obj, client_addr, msg_count):
        threading.Thread.__init__(self)
        self.client = client_obj
        self.client_addr = client_addr
        self.count = msg_count

    def run(self):
        for i in range(self.count):
            self.client.send(time.ctime().encode('utf-8'))
            time.sleep(1)
        self.client.send('close'.encode('utf-8'))
        self.client.close()
        print('[=] Client : {} connection is closed.'.format(self.client_addr))


if __name__ == '__main__':

    PORT = 9999
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    BUFSIZE = 1024
    N = 3

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(ADDR)
    print('[=] Time Server is starting at : {}'.format(ADDR))

    server_socket.listen(N)

    print('-' * 50)
    print('[=] Server waits for connection ...')

    client_list = []
    while True:
        client_socket, addr = server_socket.accept()
        print('[CONNECTED] IP & PORT at Client side {}'.format(addr))

        C = ConnectClient(client_socket, addr, 10)
        C.start()
        client_list.append(C)

        if len(client_list) == N:
            print('[=] Server has reached to maximum connections ...')
            break

    server_socket.close()
    print('[=] Server is closed')