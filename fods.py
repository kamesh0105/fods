import pandas as pd
data=pd.read_csv("C:\\Users\\MSDK\\fodspro.csv")
print('dataset')
print()
print(data)
features=data.columns
print('features in the dataset:')
print()
dtypes=data.dtypes
print(dtypes)
summary=data.describe()
print()
print('five point summary of the features:')
print(summary)
print()
print('first five rows of the dataset')
print()
print(data.head())