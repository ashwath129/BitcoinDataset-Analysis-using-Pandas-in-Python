#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


file_path = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/bh.csv'


# In[6]:



data = pd.read_csv(file_path, sep='\t', header=None)


# In[7]:


data.columns = ['blockID', 'hash', 'timestamps', 'n_Txns']


# In[8]:


df = pd.DataFrame(data) 


# In[10]:


print(df['n_Txns'].sum())


# In[11]:


file_path2 = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/addresses.csv'


# In[12]:


data2 = pd.read_csv(file_path2, sep='\t', header=None)


# In[13]:


data2.columns = ['addrID', 'addr']


# In[15]:


df2 = pd.DataFrame(data2) 


# In[17]:


print(df2['addrID'].count())


# In[ ]:




