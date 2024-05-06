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
print(df2.head(10))

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