#!/usr/bin/env python
# coding: utf-8

# In[309]:


import pandas as pd 
import numpy as np
import re
import os


# In[310]:


import time


# In[311]:


# Settings GitHub Path: 
url = 'https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv'
fields = ['Object ID','Dimensions']


# In[312]:


# Loading file
df = pd.read_csv(url,sep=',',encoding = 'utf8', usecols=fields) # skipinitialspace=True,
df.head(5)


# In[313]:


df_0 = df.dropna()


# def clean_alt_list(list_):
#     list_ = list_.replace('[(]', "|", case = False) 
#     list_ = list_.replace('[)]', "|", case = False)
#     list_ = list_.replace('[×]', "x", case = False)
#     return list_

# In[314]:


# overwriting column with replaced value of age  
df_1_0 = df_0['Dimensions'].str.replace('[)]', "|", case = False)
# overwriting column with replaced value of age  
df_1_1 = df_1_0.str.replace('[(]', "|", case = False) 
# 
df_1_2 = df_1_1.str.replace('[×]', "x", case = False)
#
df_1_3 = df_1_2.str.split('[|]',n=3, expand=True)
#
df_1_3


# In[315]:


df_1_3.columns


# In[316]:


dropCol_3 = [0,2]
df_1_4 = df_1_3.drop(columns = dropCol_3 , axis = 1, inplace = False) 


# In[317]:


df_1_4


# In[330]:


df_medida_1_1 =df_1_4[1].str.replace('cm' , "", case = False).to_frame()
df_medida_1_1


# In[331]:


df_medida_1  = df_medida_1_1[1].str.split(" x ",expand=True)
df_medida_1


# In[320]:


df_meas_1 = df_medida_1.rename(columns={0: "H1", 1: "W1", 2:"D1"}).drop(columns = [3,4]).fillna(0)


# In[332]:


df_medida_2_1 = df_1_4[3].str.replace('[|]' , " ", case = False).to_frame()
df_medida_2_2 = df_medida_2[3].str.replace('cm' , "", case = False).to_frame()
df_medida_2_2.tail()


# In[333]:


df_medida_2_3 = df_medida_2_2[3].str.split(" x ",n=2,expand=True)
df_medida_2_3


# In[334]:


df_meas_2= df_medida_2_3.rename(columns={0: "H2", 1: "W2", 2:"D2"}).fillna(0)
df_meas_2


# In[335]:


mergDf = df.merge(df_meas_1, left_index=True, right_index=True)
mergDf


# In[336]:


mergedDf = mergDf.merge(df_meas_2, left_index=True, right_index=True)
mergedDf 


# In[337]:


df_etl = mergedDf.drop(columns = ['Dimensions']).rename(columns={'Object ID': "Object_ID"})
df_etl.to_pickle("./df_etl.pkl")
df_etl


# In[380]:


ObjectID = input("Object ID: ")
# print("Object ID: " + ObjectID)




