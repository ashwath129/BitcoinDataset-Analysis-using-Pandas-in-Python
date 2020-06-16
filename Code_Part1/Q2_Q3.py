#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


file_pathout = 'D:/Blockchain/Hw 2/data/txout.csv'


# In[3]:


file_pathin = 'D:/Blockchain/Hw 2/data/txin.csv'


# In[ ]:





# In[ ]:





# In[6]:


datain = pd.read_csv(file_pathin, sep='\t', header=None)


# In[7]:


dataout = pd.read_csv(file_pathout, sep='\t', header=None)


# In[8]:


datain.columns = ['txID', 'input_seq', 'prev_txID', 'prev_output_seq', 'addrID', 'sum']


# In[9]:


dataout.columns = ['txID', 'output_seq', 'addrID', 'sum']


# In[24]:


dataSum_in = pd.DataFrame(datain.groupby(['addrID'])['sum'].sum())


# In[25]:


dataSum_out = pd.DataFrame(dataout.groupby(['addrID'])['sum'].sum())


# In[26]:


print(dataSum_out)


# In[27]:


print(dataSum_in)


# In[28]:


ans = pd.merge(dataSum_in, dataSum_out,how='right',on = 'addrID')


# In[29]:


ans=ans.fillna(0)


# In[30]:


print(ans)


# In[31]:


ans['balance'] = ans['sum_y'] - ans['sum_x']


# In[32]:


print(ans)


# In[33]:


print(ans['balance'].max())


# In[42]:


ans.loc[ans['balance'].idxmax()]


# In[35]:


print(ans['balance'].sum()/8385061)  #Answer for Question 3 in Part 1


# In[ ]:




