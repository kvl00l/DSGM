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
df[['BMI', 'Glucose']].plot.line(figsize=(20, 10), color={"BMI": "red", "Glucose": "blue"})
plt.title('Kevin')
plt.show()