#!/usr/bin/env python
# coding: utf-8

# ## Problem 1

# In[1]:


import pandas as pd


# In[2]:


#Input the cars.csv file
cars = pd.read_csv('cars.csv')
cars


# In[3]:


#Print first 5 rows 
cars.head() 


# In[4]:


#print last 5 rows
cars.tail() 

