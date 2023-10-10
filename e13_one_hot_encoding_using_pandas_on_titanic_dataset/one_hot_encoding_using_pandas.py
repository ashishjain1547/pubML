from sklearn.datasets import load_iris
data = load_iris()

# >>> list(data.target_names)
# ['setosa', 'versicolor', 'virginica']

# print(data)

# Attribute Information:       
# - sepal length in cm
# - sepal width in cm        
# - petal length in cm        
# - petal width in cm

# What we observed in the dataset is that the labels are encoded using the Ascending-Alphabetical-Sequence.

import pandas as pd
df = pd.read_csv('titanic_train.csv')
print(df.head())

print("Number of Unique Values in The Column 'Sex':")
print(df['Sex'].nunique())
# 2
# This is also the width of one-hot encoding.

print("Number of Unique Values in The Column For 'Passenger Class':")
print(df['Pclass'].nunique())
# 3
# This is also the width of one-hot encoding for 'Passenger Class'.

# Let us first see what happens when we do one-hot encoding of Sex.

enc_gender_df = pd.get_dummies(df, columns = ['Sex'])
print(enc_gender_df.head())

# Sex
# male
# female
# female
# female

# Sex_female  Sex_male
# 0                    1
# 1                    0
# 1                    0
# 1                    0
# 0                    1

enc_pc_df = pd.get_dummies(df, columns = ['Pclass'])
print(enc_pc_df.head())

# Pclass_1  Pclass_2  Pclass_3
# 0               0                1
# 1               0                0
# 0               0                1
# 1               0                0
# 0               0                1
