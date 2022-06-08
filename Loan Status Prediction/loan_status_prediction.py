# -*- coding: utf-8 -*-
"""Loan Status Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D0T-_21i3UmHdIkYCPb6jR9zCEC1MYeS
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

loan_dataset = pd.read_csv('/content/dataset.csv')

loan_dataset.head()

loan_dataset.tail()

loan_dataset.shape

loan_dataset.describe()

loan_dataset.isnull().sum()

loan_dataset.dropna(inplace= True)

loan_dataset.info()

loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)

loan_dataset.head()

loan_dataset['Dependents'].value_counts()

loan_dataset.replace(to_replace='3+', value=4, inplace=True)

sns.countplot(x='Education',hue='Loan_Status',data=loan_dataset)

sns.countplot(x='Married',hue='Loan_Status',data=loan_dataset)

loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

loan_dataset.head()

X = loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = loan_dataset['Loan_Status']

X_train, X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state= 42)

classifier = LogisticRegression()
classifier.fit(X_train,Y_train)

X_train_prediction = classifier.predict(X_train)
training_data_accuray = accuracy_score(X_train_prediction,Y_train)
print('Accuracy on training data : ', training_data_accuray)

X_test_prediction = classifier.predict(X_test)
test_data_accuray = accuracy_score(X_test_prediction,Y_test)
print('Accuracy on test data : ', test_data_accuray)