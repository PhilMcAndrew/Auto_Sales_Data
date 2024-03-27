#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path= r'C:\Users\48725\OneDrive\Pulpit\Auto Sales data.csv'


# In[22]:


df= pd.read_csv(path, sep= ',', encoding= 'utf-8', decimal= '.', on_bad_lines='warn')


# In[16]:


df.head()


# In[17]:


df.describe()


# In[19]:


df.info()


# In[20]:


pd.isnull(df)


# In[25]:


df['QUANTITYORDERED'].mean()


# In[28]:


fig= plt.figure()


# In[ ]:




