#!/usr/bin/env python
# coding: utf-8

# # Importing The Dependencies

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics


# #Data Collection & Analysis

# In[2]:


#loading the dataset from csv file to a Pandas DataFrame
big_mart_data = pd.read_csv('Train.csv')


# In[3]:


# first 5 rows of the dataframe
big_mart_data.head()


# In[4]:


#number of data points & number of Feature
big_mart_data.shape


# In[5]:


#getting some information about the dataset
big_mart_data.info()


# CategoricalFeatures:
# 
# - Item_identifier
# - Item_FAt_Content
# - Item_Type
# - Outlet_Identifier
# - Outlet_Size
# - Out_location_Type
# - Outlet_Type

# In[6]:


#checking for missing values

big_mart_data.isnull().sum()


# #Handling Missing Values
# 
# Mean -> average value
# 
# Mode -> Most repeat Value

# In[7]:


#Mean value of "Item Weight" column

big_mart_data['Item_Weight'].mean()


# In[8]:


#filling the missing values in "Item_weight" column with "mean" value

big_mart_data['Item_Weight'].fillna(big_mart_data['Item_Weight'].mean(),inplace=True)


# In[9]:


#checking for missing values
big_mart_data.isnull().sum()


# In[10]:


#Replacing the missing values in "Outlet_size" with mode
mode_of_outlet_size = big_mart_data.pivot_table(values='Outlet_Size',columns='Outlet_Type',aggfunc=(lambda x: x.mode()[0]))


# In[11]:


print(mode_of_outlet_size)


# In[12]:


missing_values = big_mart_data['Outlet_Size'].isnull()


# In[14]:


print(missing_values)


# In[88]:


# Replace NaN with 'Unknown'
big_mart_data['Outlet_Size'].fillna('Unknown', inplace=True)

# Confirm no missing values
print(big_mart_data['Outlet_Size'].isnull().sum())


# In[89]:


#checking for missing values
big_mart_data.isnull().sum()


# In[90]:


# statistical measure about the data
big_mart_data.describe()


# Numerical Feature

# In[91]:


sns.set()


# In[92]:


#Item weight distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Weight'])
plt.show()


# In[93]:


# Item_Visibility distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Visibility'])
plt.show()


# In[94]:


# Item_MRP distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_MRP'])
plt.show()


# In[95]:


# Item_Outlet_Sales distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart_data['Item_Outlet_Sales'])
plt.show()


# In[96]:


#Outlet_Establishment_Year_column
plt.figure(figsize=(6,6))
sns.countplot(x='Outlet_Establishment_Year',data=big_mart_data)
plt.show()


# In[97]:


#Item_Fat_Content column
plt.figure(figsize=(6,6))
sns.countplot(x = 'Item_Fat_Content',data = big_mart_data)
plt.show()


# In[98]:


#Item_Type column
plt.figure(figsize=(30,6))
sns.countplot(x = 'Item_Type',data = big_mart_data)
plt.show()


# In[99]:


#Outlet_size column
plt.figure(figsize=(6,6))
sns.countplot(x ='Outlet_Size',data = big_mart_data)
plt.title('Item_Type_count')
plt.show()


# #Data Pre-processing
# 

# In[100]:


big_mart_data['Item_Fat_Content'].value_counts()


# In[101]:


big_mart_data.replace({'Item_Fat_Content':{'low fat':'Low Fat','LF':'Low Fat' , 'reg' : 'Regular'}},inplace = True)


# In[102]:


big_mart_data['Item_Fat_Content'].value_counts()


# Label Encoding 

# In[103]:


encoder = LabelEncoder()


# In[104]:


big_mart_data['Item_Identifier'] = encoder.fit_transform(big_mart_data['Item_Identifier'])


# In[105]:


big_mart_data['Item_Fat_Content'] = encoder.fit_transform(big_mart_data['Item_Fat_Content'])


# In[106]:


big_mart_data['Item_Type'] = encoder.fit_transform(big_mart_data['Item_Type'])


# In[107]:


big_mart_data['Outlet_Identifier'] = encoder.fit_transform(big_mart_data['Outlet_Identifier'])


# In[108]:


big_mart_data['Outlet_Size'] = encoder.fit_transform(big_mart_data['Outlet_Size'])


# In[ ]:





# In[109]:


big_mart_data.head()


# Splitting Feature and Target

# In[110]:


X = big_mart_data.drop(columns='Item_Outlet_Sales',axis=1)
Y = big_mart_data['Item_Outlet_Sales']


# In[111]:


print(X)


# Splitting the data into Training data & Testing Data

# In[116]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)


# Machine Learning Model Training

# XGBoost Regressor

# In[117]:


regressor = XGBRegressor()


# In[118]:


regressor.fit(X_train,Y_train)


# #Evaluation

# In[119]:


# Prediction on training data
training_data_prediction = regressor.predict(X_train)


# In[120]:


#R squared Value
r2_train = metrics.r2_score(Y_train,training_data_prediction)


# In[121]:


print('R Squared Value = ',r2_train)


# In[ ]:


# Prediction on Test Data

