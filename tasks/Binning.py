import pandas as pd
import numpy as np
import logging

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

df = pd.read_csv("../data/dataset.csv")
logger.info("Dataset loaded for binning.")

# Distance binning
min_value = df['ApplicantIncome'].min()
max_value = df['ApplicantIncome'].max()
logger.info(f"Min Income: {min_value}, Max Income: {max_value}")

# Bin size is 5
bins = np.linspace(min_value, max_value, 5)
logger.info(f"Bins: {bins}")

labels = ['Juvenile', 'Adult', 'Middle Age', 'Senior Citizen']

# Cut function for distance binning
df['bins_dist'] = pd.cut(df['ApplicantIncome'], bins=bins, labels=labels, include_lowest=True)
logger.info(f"Distance Binning Results:\n{df['bins_dist']}")

# Frequency binning
df['bin_freq'] = pd.qcut(df['ApplicantIncome'], q=4, precision=1, labels=labels)
logger.info(f"Frequency Binning Results:\n{df['bin_freq']}")
