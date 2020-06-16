#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


file_path = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/addr_sccs.dat'


# In[3]:


data = pd.read_csv(file_path, sep='\t', header=None)


# In[4]:


data.columns = [ 'addrID', 'userId']


# In[5]:


df = pd.DataFrame(data)


# In[8]:


print(df['userId'].count())


# In[11]:


print(df.drop_duplicates('userId').count())


# In[ ]:




