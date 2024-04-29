#
# Kevin
# Pandas practice
#

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r'D:\DATA Science\DSGM\smoker.csv')

# Inspect structure
df.shape
df.info()

# Inspect value
df.head()
df.tail()

# Visualize
df['smoker'].hist()
#plt.show()

# Count rows of same value
print(df['smoker'].value_counts())
print(df['treatment'].value_counts())
print(df['outcome'].value_counts())

# Mean
print(df['smoker'].mean())
print(df['treatment'].mean())
print(df['outcome'].mean())

# Sum
print(df.sum())
print(df.sum(axis = 1))