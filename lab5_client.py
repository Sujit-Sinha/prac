import socket

PORT = 9999

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
BUFSIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

client_socket.connect(ADDR)

while True:
    msg = client_socket.recv(BUFSIZE).decode()
    if msg == 'close':
        break

    print('[=] Message from server : {}'.format(msg))

client_socket.close()