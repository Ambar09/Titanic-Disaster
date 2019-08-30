#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Installing all the libraries

import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series,DataFrame

#for stats
from scipy import stats

#for plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#to see the plotting inline
get_ipython().magic(u'matplotlib inline')


# In[2]:


Titanic_df = pd.read_clipboard() #Reading the csv file


# In[3]:


Titanic_df.head()


# In[4]:


Titanic_df.info() #Getting the summary of the dataframe


# In[5]:


Titanic_df['Person'] = np.where(Titanic_df['Age']<16,'Child',Titanic_df.Sex) #Creating a new column in a dataframe


# In[7]:


Titanic_df.head(10)


# In[8]:


#Univariate Analysis
sns.factorplot(x = 'Sex', data = Titanic_df, kind = 'count') #To know the count of each gender in the dataset


# In[9]:


sns.factorplot(x = 'Sex', data = Titanic_df, kind = 'count', hue = 'Pclass') #To know the gender in each class


# In[10]:


sns.factorplot(x = 'Pclass', data = Titanic_df, kind = 'count', hue = 'Sex') #To know the gender in each class


# In[11]:


sns.factorplot(x = 'Pclass', data = Titanic_df, kind = 'count', hue = 'Person') #To know the male, female and 
# children in each class


# In[12]:


Titanic_df['Age'].hist(bins =70, ec = 'black') #Age Distribution


# In[13]:


Titanic_df.Age.mean()


# In[15]:


fig = sns.FacetGrid(Titanic_df, hue = 'Person', aspect= 4)

fig.map(sns.kdeplot, 'Age', shade = True)

oldest = Titanic_df['Age'].max()

fig.set(xlim = (0,oldest)) # X axis from zero to oldest age

fig.add_legend()


# In[16]:


fig = sns.FacetGrid(Titanic_df, hue = 'Pclass', aspect= 4)

fig.map(sns.kdeplot, 'Age', shade = True)

oldest = Titanic_df['Age'].max()

fig.set(xlim = (0,oldest)) # X axis from zero to oldest age

fig.add_legend()


# In[17]:


Cabin_New = Titanic_df['Cabin'].dropna() #Droppping NA values from Cabin column


# In[19]:


Cabin_New.head()


# In[22]:


levels = [] #Created a list and put all the 1st characters of cabin column in that list

for level in Cabin_New:
    levels.append(level[0])
    
Cabin_df = DataFrame(levels)


# In[25]:





# In[27]:


Cabin_df.columns = ['Cabin'] # Changed the name of column


# In[28]:


Cabin_df.head()


# In[33]:


sns.factorplot(x = 'Cabin', data = Cabin_df, kind = 'count', palette = 'summer')


# In[35]:


sns.factorplot(x = 'Embarked', data = Titanic_df, kind = 'count', palette = 'winter', hue = 'Pclass') #Distribution of Embarked Column


# In[36]:


#To check if the person was alone or not

Titanic_df['Alone'] = Titanic_df['SibSp'] + Titanic_df['Parch']


# In[37]:


Titanic_df.head()


# In[41]:


Titanic_df['Alone_or_not'] = np.where(Titanic_df['Alone']==0,'Alone','With Family') #Created a new column to tell
#if the person was travelling alone or not.


# In[42]:


Titanic_df


# In[43]:


sns.factorplot(x = 'Alone_or_not', data = Titanic_df, kind = 'count')


# In[ ]:


sns.factorplot(x = 'Alone_or_not', data = Titanic_df, kind = 'count', hue = 'Pclass')


# In[48]:


sns.factorplot(x = 'Person', y ='Survived', hue = 'Pclass', data = Titanic_df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[32]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




