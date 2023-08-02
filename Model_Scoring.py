#!/usr/bin/env python
# coding: utf-8

# # Data Load

# In[17]:


import pandas as pd
import os
import glob

path = os.getcwd()
path=path+"\\Input"
csv_files = glob.glob(os.path.join(path, "*.csv"))


# In[18]:


data = pd.read_csv(csv_files[0], delimiter = ':',low_memory=False)
data.head(5)


# In[3]:


import numpy as np
try:
    data['Match_Flag']= np.where(data['matched_transaction_id'] == data['feature_transaction_id'],1,0) 
except:
    data['Match_Flag']=""


# In[4]:


#Keeping only the required columns
data_v1=data[[ 'DateMappingMatch',
 'AmountMappingMatch',
 'DescriptionMatch',
 'DifferentPredictedTime',
 'TimeMappingMatch',
 'PredictedNameMatch',
 'ShortNameMatch',
 'DifferentPredictedDate',
 'PredictedAmountMatch',
 'PredictedTimeCloseMatch','Match_Flag']]


# In[5]:


#Drop the three variables 
data_v1 = data_v1.drop(columns=['DifferentPredictedDate', 'DifferentPredictedTime','DateMappingMatch'])


# In[6]:


data_v1.head()


# In[7]:


#load model
import pickle
rfm_clf = pickle.load(open('Model\\random_forest_model.pkl', 'rb'))


# In[8]:


proba = rfm_clf.predict_proba(data_v1[[ 
#'DateMappingMatch',
 'AmountMappingMatch',
 'DescriptionMatch',
 #'DifferentPredictedTime',
 'TimeMappingMatch',
 'PredictedNameMatch',
 'ShortNameMatch',
 #'DifferentPredictedDate',
 'PredictedAmountMatch',
 'PredictedTimeCloseMatch']])[:,1]


# In[9]:


proba=pd.DataFrame(proba)
proba.columns=['probability']


# In[10]:


data_scored=pd.concat([data,proba],axis=1)


# In[12]:


data_scored.sort_values(by="probability",ascending=False,inplace=True)


# In[25]:


path2 = os.getcwd()
path2=path2+"\\Output"
data_scored.to_csv(path2+"\Scored.csv", index=False)

