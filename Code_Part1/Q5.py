#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


file_path = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/tx.csv'


# In[3]:


data = pd.read_csv(file_path, sep='\t', header=None)


# In[4]:


data.columns = ['txid', 'blockid', 'n_input', 'n_output']


# In[5]:


df = pd.DataFrame(data) 


# In[6]:


df.loc[df['n_input'].idxmax]


# In[7]:


file_path2 = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/txh.csv'


# In[8]:


data2 = pd.read_csv(file_path2, sep='\t', header=None)


# In[9]:


data2.columns = ['txid', 'hash']


# In[11]:


df2 = pd.DataFrame(data2) 


# In[12]:


df2.loc[df['txid'] == 7553001]


# In[ ]:




