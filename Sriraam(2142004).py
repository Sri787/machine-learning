#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# In[11]:


df=pd.read_csv(r"D:\Download\archive (1)\framingham.csv")


# In[12]:


df


# In[13]:


df.info()


# In[14]:


df.describe()


# In[15]:


df.isnull().sum()


# In[16]:


df.shape


# In[17]:


fig = plt.figure(figsize =(10, 7))
plt.boxplot(df)
plt.show()


# In[18]:


fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)
axs.hist(df) 
plt.show()


# In[19]:


df['education'].mode()


# In[20]:


df['cigsPerDay'].interpolate()
print(df)


# In[21]:


df['education'].fillna((df['education'].mean()), inplace=True)
print(df)


# In[22]:


df.isnull().sum()


# In[23]:


a=df['totChol'].mean()


# In[24]:


df['totChol'].fillna(a,inplace=True)


# In[25]:


df.isnull().sum()


# In[26]:


b=df['BMI'].mean()


# In[27]:


df['BMI'].fillna(b,inplace=True)


# In[28]:


df.isnull().sum()


# In[29]:


c=df['education'].mode().index[0]


# In[30]:


df['education'].fillna(c,inplace=True)


# In[31]:


df.isnull().sum()


# In[32]:


d=df['BPMeds'].mode()


# In[33]:


df['BPMeds'].fillna(d[0],inplace=True)


# In[34]:


df.isnull().sum()


# In[35]:


e=df['cigsPerDay'].mode()


# In[36]:


df['cigsPerDay'].fillna(e[0],inplace=True)


# In[37]:


df.isnull().sum()


# In[38]:


f=df['glucose'].mode()


# In[39]:


df['glucose'].fillna(f[0],inplace=True)


# In[40]:


df.isnull().sum()


# In[44]:


df.isnull().sum()


# In[45]:


df.info()


# In[46]:


import matplotlib


# In[47]:


import matplotlib.pyplot as plt


# In[48]:


fig = plt.figure(figsize =(10, 7))
plt.boxplot(df)
plt.show()


# In[49]:


fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)
axs.hist(df) 
plt.show()


# In[50]:


import seaborn as sns


# In[51]:


sns.heatmap(df.corr(),annot=True,cmap='RdYlGn',linewidths=0.2)
fig=plt.gcf()
fig.set_size_inches(50,50)
plt.show()


# In[54]:


plt.scatter(df['age'],df['BMI'])
plt.xlabel('AGE')
plt.ylabel('BMI')
plt.title('Age vs BMI')
plt.show()


# In[53]:


plt.plot(df['age'],df['BMI'])
plt.show()


# In[ ]:




