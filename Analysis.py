import pandas as pd

df = pd.read_csv('data/sales dataset.csv')

#   Option 1: Allows the full Data
#print(df)

# Option 2: This allows to show the first few rows [LIMITS]
#print(df.head())

# Option 3: This allows to show the last few rows [LIMITS]
#print(df.tail())

# This shows the structure of the Data [Colum. Names/Data Type/Missing Values]
#print(df.info())