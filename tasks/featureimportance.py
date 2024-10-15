# URL Ref - https://machinelearningmastery.com/calculate-feature-importance-with-python/
# For the Covid Dataset, show the feature importance for:
# 1. Decision Tree - CART Feature Importance
# 2. Random Forest
# 3. Permutation Feature Importance - KNN 

# Demonstrate various Feature Selection Techniques on the "Covid" dataset
# URL for reference - https://www.analyticsvidhya.com/blog/2020/10/feature-selection-techniques-in-machine-learning/

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer


df = pd.read_csv("../data/dataset.csv")
df['Dependents'].value_counts()
df = df.replace(to_replace='3+', value=4)
df['Dependents'].value_counts()
df['Loan_ID'] = df['Loan_ID'].str.replace('LP00', '', regex=False)
df.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)
X = df.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = df['Loan_Status']
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)
print(X)
print(Y)
X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)
print(X.shape, X_train.shape, X_test.shape)
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train,Y_train)
X_train_prediction = classifier.predict(X_train)
training_data_accuray = accuracy_score(X_train_prediction,Y_train)
print('Accuracy on training data : ', training_data_accuray)
X_test_prediction = classifier.predict(X_test)
test_data_accuray = accuracy_score(X_test_prediction,Y_test)
print('Accuracy on test data : ', test_data_accuray)
