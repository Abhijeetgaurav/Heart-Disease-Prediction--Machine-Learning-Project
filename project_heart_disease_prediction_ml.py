# -*- coding: utf-8 -*-
"""Project: Heart disease prediction ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jE2Zq2EvCIwpWLkHohMVK24H6F9UMFLP
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('/content/heart_disease_data.csv')

df.head()

df.shape

df.info()

df.isnull().sum()

#statiscal measure about the data
df.describe()

#checking the distribution of Target Variable
df['target'].value_counts()

"""0----> healthy heart
1----> defective heart
"""

#spliting the features and target
X = df.drop(columns='target',axis=1)
Y = df['target']

print(X)

print(Y)

#splitting the data into trianing and testing data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,stratify=Y,random_state=2)
# stratify means it will distribute the two category of target uniformly

print(X.shape,X_train.shape,X_test.shape)

"""model training and we are using Logistic regression and binary classification"""

model = LogisticRegression()

#training the logistic regression model with training data
model.fit(X_train,Y_train)

"""model evaluation

Accuracy Score
"""

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('Acuracy on training data: ',training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print('Acuracy on test data: ',test_data_accuracy)

"""accuracy score of training and test data should be nearly same

if the accuracy score of training data is more and of testing is low then the model is overfitted

Going to build a predective system
"""

input_data = (64,1,3,110,211,0,0,144,1,1.8,1,0,2)
#change the input data to a numpy array
# as array ---> convert datatype to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for only one instance
input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshape)
print(prediction)

if(prediction[0]==0):
  print('The person does not have heart disease')
else:
  print('The person has heart disease')

