#
# Kevin
# Pandas Practice
#

# Diabetes
import pandas as pd
df = pd.read_csv('D:\DATA Science\DSGM\Pandasi\diabetes.csv')

# Inspect structure
df.shape
df.info()

# Add missing values
df2 = df.copy()
df2.loc[2:5,'Pregnancies'] = None

# Print df2
df2.head(10)

# Add missing values
df2.isnull().sum()
df2.shape

# Remove rows with missing value
df3 = df2.copy()
df3 = df3.dropna()

# Remove rows with missing value
df3.shape

# Creating new columns based on other columns
df2['Glucose_Insulin_Ratio'] = df2['Glucose'] / df2['Insulin']
df2.head()

# Count by value
df['Outcome'].value_counts()
df['Outcome'].value_counts(sort = False)

# By group
df.groupby('Outcome').mean()

# By group
df.groupby(['Pregnancies', 'Outcome']).mean()
df.groupby(['Pregnancies', 'Outcome']).value_counts()
df.groupby(['Pregnancies', 'Outcome']).value_counts(normalize = True)

# Improt plt 
import matplotlib.pyplot as plt

# Visual BMI
df[['BMI', 'Glucose']].plot.line()
plt.title('Kevin')
plt.show()


df[['BMI', 'Glucose']].plot.line(figsize=(20, 10), color={"BMI": "red", "Glucose": "blue"})
plt.show()