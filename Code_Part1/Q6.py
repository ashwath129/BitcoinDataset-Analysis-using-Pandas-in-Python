#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


file_path = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/txout.csv'


# In[3]:


data = pd.read_csv(file_path, sep='\t', header=None)


# In[7]:


data.columns = ['txID','output_seq', 'addrID', 'sum']


# In[8]:


df = pd.DataFrame(data)


# In[16]:


txids = df.drop_duplicates('txID')


# In[17]:


txidCount = txids['txID'].count()


# In[18]:


sum = df['sum'].sum()


# In[19]:


avgValue = sum / txidCount


# In[20]:


print(avgValue)


# In[ ]:




