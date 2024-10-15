from tkinter import TRUE
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("../data/dataset.csv")
print(df)

numerical_df = df.select_dtypes(include=[np.number])

# Correlation Matrix - Internally uses Pearson Correlation
cor = numerical_df.corr()

# Plotting Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(cor, annot=True)
plt.show()

# Correlation Matrix - Internally uses Pearson Correlation
# cor = df.corr()

# # Plotting Heatmap
# plt.figure(figsize = (10,6))
# sns.heatmap(cor, annot=True)
# plt.show()