import socket
import time

# Settings:
PORT=12002
# SERVER='192.168.0.108'
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)
BUFSIZE=1024
FORMAT='utf-8'

# Create the TCP socket object:
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket object to PORT:
server_socket.bind(ADDR)
print('[=] Time Server is starting at : {}'.format(ADDR))

# Start listening:
server_socket.listen(1)

print('-'*50)
print('[=] Server waits for connection ...')
client_socket, addr=server_socket.accept()
print('[CONNECTED] IP & PORT at Client side {}'.format(addr))

while True:
    # Send MSG to client:
    msg=time.ctime()
    # client_socket.send(bytes(msg,FORMAT))
    client_socket.send(msg.encode(FORMAT))

    # Check client reply
    print('Waiting for client reply')
    msg=client_socket.recv(BUFSIZE).decode()
    if msg=='close':
        # Close client connection:
        client_socket.close()
        break

# CLose server:
server_socket.close()

