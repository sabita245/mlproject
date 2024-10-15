# Demonstrate One-hot encoding and Label encoding in Python
# 1. Importing the Libraries
import pandas as pd
import numpy as np
 
# 2. Reading the file
df = pd.read_csv("../data/dataset.csv")
df['Dependents'].value_counts()
df = df.replace(to_replace='3+', value=4)
df['Dependents'].value_counts()
df['Loan_ID'] = df['Loan_ID'].str.replace('LP00', '', regex=False)
df.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)
print(df)

