from tkinter import TRUE
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
df = pd.read_csv("../data/dataset.csv")
logger.info("dataset load successfully")

numerical_df = df.select_dtypes(include=[np.number])

# Correlation Matrix - Internally uses Pearson Correlation
cor = numerical_df.corr()

# Plotting Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(cor, annot=True)
plt.show()

