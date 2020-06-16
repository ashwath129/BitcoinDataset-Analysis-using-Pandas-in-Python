#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np


# In[9]:


file_out = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/txout.csv'


# In[10]:


dfout = pd.read_csv(file_out, sep='\t')


# In[12]:


dfout.columns=['txID','output_seq','addrID','sum']


# In[13]:


df = pd.DataFrame(dfout.drop_duplicates('addrID'))


# In[14]:


transOutCount = dfout['txID'].count()


# In[15]:


addrCnt= df['addrID'].count()


# In[16]:


transOutCount / addrCnt


# In[17]:


file_in = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/txin.csv'


# In[18]:


dfin = pd.read_csv(file_in, sep='\t')


# In[19]:


dfin.columns=['txID','input_seq','prev_txID','prev_output_seq','addrID', 'sum']


# In[20]:


tcount = dfin['txID'].count()


# In[21]:


addr_in = pd.DataFrame(dfin.drop_duplicates('addrID'))


# In[22]:


addrCount = addr_in['addrID'].count()


# In[23]:


tcount / addrCount


# In[24]:


pd.concat([dfout, dfin])


# In[25]:


tabCombined = pd.concat([dfout, dfin])


# In[26]:


addresses = pd.DataFrame(tabCombined.drop_duplicates('addrID'))


# In[27]:


totalAddr = addresses['addrID'].count()


# In[28]:


AvgPerAddr =  (tcount + transOutCount) / totalAddr


# In[29]:


print(AvgPerAddr)


# In[ ]:




