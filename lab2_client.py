import socket

# Settings:
PORT=12002
# SERVER='192.168.0.108'
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)
BUFSIZE=1024
FORMAT='utf-8'

# Create the TCP socket object:
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect client socket object to PORT:
client_socket.connect(ADDR)
print('[=] Client is connecting to IP & PORT at Server side {}'.format(ADDR))

while True:
    # Collect the message from server:
    # data=client_socket.recv(BUFSIZE)
    # msg=data.decode(FORMAT)
    msg=client_socket.recv(BUFSIZE).decode()
    print('[=] Message from server : {}'.format(msg))

    flag=input('Close connection y/n : ')
    # Send message to server:
    if flag=='y' or flag=='Y':
        client_socket.send('close'.encode(FORMAT))
        # Close client socket:
        client_socket.close()
        break

    else:
        client_socket.send(('Received - '+msg).encode(FORMAT))