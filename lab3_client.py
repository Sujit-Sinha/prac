import socket
# Settings:
PORT=9090
# SERVER='192.168.0.108'
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)
BUFSIZE=1024
FORMAT='utf-8'
# Create the UDP socket object:
client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Connect client socket object to PORT:
client_socket.sendto(str.encode('Hello', FORMAT), ADDR)
print('[=] Client is connecting to IP & PORT at Server side {}'.format(ADDR))
while True:
   # Collect the message from server:
   msg, addr=client_socket.recvfrom(BUFSIZE)
   msg=msg.decode()
   print('[=] Message from server {} : {}'.format(addr,msg))
   flag=input('Close connection y/n : ')
   # Send message to server:
   if flag=='y' or flag=='Y':
     client_socket.sendto('close'.encode(FORMAT), ADDR)
     client_socket.close()
     break
   else:
     client_socket.sendto(('Received - '+msg).encode(FORMAT), ADDR)