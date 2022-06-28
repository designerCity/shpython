#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd


# In[9]:
two_dimensional_list = [['세형', 90, 30], ['수민', 50, 100], ['준성', 80, 88]]


# In[12]:


data = pd.DataFrame(two_dimensional_list, columns=['이름', '수학 성적', '국어 성적'], index=['a','b','c'])
data


# data type 을 살펴보면, pandas DataFrame이라고 나온다. 

# In[11]:


type(data)


# In[14]:


data.columns


# In[15]:


data.index


# In[17]:


data.dtypes


# In[26]:


import pandas as pd


# In[30]:


df_2016 = pd.read_csv(r'./Desktop/전남권.csv', encoding='cp949')
df_2016


# ## header 가 없는 경우

# In[32]:


df_2016 = pd.read_csv(r'./Desktop/전남권.csv', header=None, encoding='cp949')


# ### header=None

# ## 0번 column 을 빼내주기

# In[34]:


df_2016 = pd.read_csv(r'./Desktop/전남권.csv', index_col=0 ,encoding='cp949')
df_2016


# In[ ]:




