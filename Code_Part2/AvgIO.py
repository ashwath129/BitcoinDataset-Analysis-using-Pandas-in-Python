#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


file_out = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/txout.csv'


# In[6]:


dfout = pd.read_csv(file_out, sep='\t')


# In[7]:


dfout.columns=['txID','output_seq','addrID','sum']


# In[27]:


df = pd.DataFrame(dfout.drop_duplicates('addrID'))


# In[28]:


transOutCount = dfout['txID'].count()


# In[29]:


addrCnt= df['addrID'].count()


# In[45]:


transOutCount / 4318422


# In[31]:


file_in = 'D:/Ash/UFL/Sem2/Blockchain Optimization and Applications/HW2/compressed/data/txin.csv'


# In[32]:


dfin = pd.read_csv(file_in, sep='\t')


# In[33]:


dfin.columns=['txID','input_seq','prev_txID','prev_output_seq','addrID', 'sum']


# In[34]:


tcount = dfin['txID'].count()


# In[35]:


addr_in = pd.DataFrame(dfin.drop_duplicates('addrID'))


# In[38]:


addrCount = addr_in['addrID'].count()


# In[46]:


tcount / 4318422


# In[21]:


pd.concat([dfout, dfin])


# In[22]:


tabCombined = pd.concat([dfout, dfin])


# In[23]:


addresses = pd.DataFrame(tabCombined.drop_duplicates('addrID'))


# In[24]:


totalAddr = addresses['addrID'].count()


# In[47]:


AvgPerAddr =  (tcount + transOutCount) / 4318422


# In[48]:


print(AvgPerAddr)


# In[ ]:




