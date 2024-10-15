import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set default Seaborn theme
sns.set_theme()

# Load your dataset (ensure the path is correct)
df = pd.read_csv("../data/dataset.csv")
df['Dependents'].value_counts()
df = df.replace(to_replace='3+', value=4)
df['Dependents'].value_counts()
df['Loan_ID'] = df['Loan_ID'].str.replace('LP00', '', regex=False)
df.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

# Example of a univariate countplot
sns.countplot(x='Education', hue='Loan_Status', data=df)
plt.title('Count Plot of Education with Loan Status')
plt.show()

# --------------------------------------- UNIVARIATE ANALYSIS ------------------------------

# 1.1 Box Plot for Age
if 'Age' in df.columns:
    sns.boxplot(y=df['Age'])  # Or plt.boxplot(df['Age'])
    plt.title('Box Plot of Age')
    plt.show()

# 1.2 Strip Plot for Age
if 'Age' in df.columns:
    sns.stripplot(y=df['Age'])
    plt.title('Strip Plot of Age')
    plt.show()

# 1.3 Swarm Plot for Age
if 'Age' in df.columns:
    sns.swarmplot(x=df['Age'])
    plt.title('Swarm Plot of Age')
    plt.show()

# 1.4 Histogram for Age
if 'Age' in df.columns:
    plt.hist(df['Age'])
    plt.title('Histogram of Age')
    plt.show()

# 1.5 Distplot with corrected 'kde' parameter
if 'Age' in df.columns:
    sns.histplot(df['Age'], kde=False, color='blue', bins=5)
    plt.title('Dist Plot of Age with 5 bins')
    plt.show()

# 1.6 Countplot for Gender
if 'Gender' in df.columns:
    sns.countplot(x=df['Gender'])
    plt.title('Count Plot of Gender')
    plt.show()

# --------------------------------------- BIVARIATE ANALYSIS ------------------------------

# 2.1 Boxplot for Covid Severity vs Days of Stay
if 'ApplicantIncome' in df.columns and 'Property_Area' in df.columns:
    sns.boxplot(x=df['ApplicantIncome'], y=df['Property_Area'], data=df)
    plt.title('Box Plot of Income vs Property_Area')
    plt.show()

# # 2.2 Scatter Plot for Age vs Days of Stay
# if 'Age' in df.columns and 'DaysOfStay' in df.columns:
#     sns.scatterplot(x=df['DaysOfStay'], y=df['Age'])
#     plt.title('Scatter Plot of Age vs Days of Stay')
#     plt.show()

# # 2.3 Scatterplot with Hue (Covid Severity Description)
# if 'Covid_SeverityDescription' in df.columns:
#     sns.scatterplot(x=df['DaysOfStay'], y=df['Age'], hue=df['Covid_SeverityDescription'])
#     plt.title('Scatter Plot of Age vs Days of Stay with Covid Severity Description')
#     plt.show()

# # 2.4 FacetGrid for Gender vs Discharge Type
# if 'Gender' in df.columns and 'DischargeType' in df.columns:
#     g = sns.FacetGrid(df, col="Gender", height=6.5, aspect=.85)
#     g.map(sns.histplot, "DischargeType")
#     plt.show()

# # ----------------------------- MULTIVARIATE ANALYSIS ----------------------------------

# # 2.5 lmplot for Age vs Days of Stay with Gender hue
# if 'Age' in df.columns and 'DaysOfStay' in df.columns and 'Gender' in df.columns:
#     sns.lmplot(data=df, x="Age", y="DaysOfStay", hue="Gender")
#     plt.title('lmplot of Age vs Days of Stay with Gender')
#     plt.show()









