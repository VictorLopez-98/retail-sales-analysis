import pandas as pd
import sqlite3

df = pd.read_csv('Data/Sales Dataset.csv')

# Creates a temporary SQL database
conn = sqlite3.connect(':memory:')

# Takes the DataFrame and creates a SQL table called "sales"
df.to_sql('sales', conn, index = False)

#SQL
query = """
SELECT *
FROM 
"""

