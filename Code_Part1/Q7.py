#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[15]:


file_path = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/tx.csv'


# In[16]:


data = pd.read_csv(file_path, sep='\t', header=None)


# In[17]:


data.columns = ['txId', 'blockId', 'n_input', 'n_output']


# In[18]:


df = pd.DataFrame(data) 


# In[19]:


print(df)


# In[20]:


df.loc[df['n_input'] == 0]


# In[ ]:




