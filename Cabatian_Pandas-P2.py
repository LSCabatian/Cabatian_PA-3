#!/usr/bin/env python
# coding: utf-8

# ## Problem 2

# In[1]:


import pandas as pd


# In[29]:


#Print data frame with odd-numbered columns that contains the first five rows
odd = cars.iloc[:5,::2]
odd


# In[39]:


#Print the row for the model "Mazda RW4 Wag
cars.loc[[0]]


# In[34]:


#Print the cyl value for car model "Camaro Z28" 
cars.loc[[23],['cyl']]


# In[38]:


#Print the cyl and gear of the given model cars
cars.loc[[1,18,28],['Model','cyl','gear']] 

