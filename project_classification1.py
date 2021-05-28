# -*- coding: utf-8 -*-
"""Project_Classification1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R0EAMMCoKOHXVRkk3JHVEjhc1rRHIIaR

# Importing libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.svm import SVC

import math

from google.colab import drive
drive.mount('/content/drive')

"""# Importing Datasets"""

df=pd.read_csv('/content/drive/My Drive/CSV/hemorrhage_diagnosis.csv')
print(df.shape)
print("Successfully imported data into console" )  
df.head(10)

df.info()

"""# Plotting the graphs"""

sns.countplot(data=df)
plt.rcParams['figure.figsize']=(20.0,25.0)

"""Plotting the grapgh for people having hameorarge or not"""

sns.countplot(x='No_Hemorrhage',data=df)
plt.rcParams['figure.figsize']=(5.0,5.0)

sns.countplot(x='No_Hemorrhage',hue='Fracture_Yes_No',data=df)
plt.rcParams['figure.figsize']=(10.0,5.0)

"""# Data Wrangling 
finding out the missing values
"""

df.isnull() # will give the null value

"""No null values are found so we'll wont remove anything """

plt.rcParams['figure.figsize']=(12.0,10.0)
sns.heatmap(df.isnull(),yticklabels=False,cmap="YlGnBu")

"""# Training and testing algorithim"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix,accuracy_score
 
x = df.drop('No_Hemorrhage', axis=1)
y = df['No_Hemorrhage']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1)
logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)
 
predictions = logmodel.predict(x_test)
print('Classification Report')

print(classification_report(y_test, predictions))
print('Confusion Matrix')

print(confusion_matrix(y_test, predictions))
print('\n Accuracy Report')
print(accuracy_score(y_test, predictions))