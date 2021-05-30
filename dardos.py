#!/usr/bin/env python
# coding: utf-8

# In[19]:


entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])

if a==0 and b==0:
    print("NO ALVO!", end="")
else:
    if (a>0 and b>0):
        print("R1", end="")
    if a<0 and b<0:
        print("R3", end="")
    if a>0 and b<0:
        print("R4", end="")
    if a<0 and b>0:
        print("R2", end="")


# In[ ]:




