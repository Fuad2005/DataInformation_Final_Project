import pandas as pd

data = pd.read_csv('data.csv')
data = data.drop_duplicates()
data.to_csv('data.csv', index=False)
