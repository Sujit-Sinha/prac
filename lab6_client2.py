#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import time

# In[ ]:


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
client_port = 50000
client.bind(("", client_port))
T1 = time.time()
while True:
    data, addr = client.recvfrom(1024)
    print('[=] Recieved message from server {} is {}'.format(addr, data.decode('utf-8')))

    if (time.time() - T1) > 10:
        print("Elapsed 10s,now close client")
        client.close()
        break


