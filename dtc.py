#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import numpy as np
import pandas as pd
from sklearn import preprocessing


# In[2]:


df=pd.read_csv(r'C:\Users\Ishika Singhal\Desktop\hcl hackathon\hcl_dataset.csv')


# In[3]:


df.head()


# In[4]:


df['cough'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['tiredness'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['fever'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['sore_throat'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['aches'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['breathlessness'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['chest_pain'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['loss_of_smell'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['loss_of_taste'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['loss_of_speech'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df['travelling'].replace(to_replace=['no','yes'], value=[0,1],inplace=True)
df.head()


# In[12]:


X = df[['age', 'cough','tiredness', 'fever', 'sore_throat', 'aches', 'breathlessness', 'chest_pain','loss_of_smell', 'loss_of_taste', 'loss_of_speech', 'travelling']] .values.astype(float)
X[0:5]


# In[13]:


y = df['risk_factor'].values
y[0:5]


# In[14]:


#X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
#X[0:5]


# In[15]:


from sklearn import tree


# In[16]:


dt_clf_gini = tree.DecisionTreeClassifier(criterion = "gini", 
                                     random_state = 100, 
                                     max_depth = 5, 
                                     min_samples_leaf = 5) 
  
dt_clf_gini.fit(X,y) 


# In[17]:


import pickle
Pkl_Filename = "model.pkl"  

with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(dt_clf_gini, file)


# In[ ]:




