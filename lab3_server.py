import socket
import time
# Settings:
PORT=9090
# SERVER='192.168.0.108'
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)
BUFSIZE=1024
FORMAT='utf-8'
# Create the UDP socket object:
server_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket object to PORT:
server_socket.bind(ADDR)
print('[=] Time Server is starting at : {}'.format(ADDR))
print('-'*50)
print('[=] Server waits for connection ...')
msg, addr = server_socket.recvfrom(BUFSIZE)
print('[CONNECTED] IP at Client side {}'.format(addr))
print('[MESSAGE] Client sent - {}'.format(msg.decode()))
while True:
   # Send MSG to client:
   msg=time.ctime()
   server_socket.sendto(msg.encode(FORMAT),addr)

   # Check client reply
   print('Waiting for client reply')
   msg, addr = server_socket.recvfrom(BUFSIZE)
   if msg.decode()=='close':
     server_socket.close()
     break