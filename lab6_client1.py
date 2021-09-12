#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import time

# In[3]:


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)


# In[4]:


client_port = 50000
client.bind(("", client_port))
T1 = time.time()

# In[ ]:


while True:
    data, addr = client.recvfrom(1024)
    print('[=] Recieved message from server {} is {}'.format(addr, data.decode('utf-8')))

    if (time.time() - T1) > 20:
        print("Elapsed 20s,now close client")
        client.close()
        break

# In[ ]:




