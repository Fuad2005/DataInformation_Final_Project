import pandas as pd


data = pd.read_csv('data.csv')


data['temp_price'] = data['price'].str.replace(' AZN', '')
data['temp_price'] = data['temp_price'].str.replace(' ', '')
data['temp_price'] = data['temp_price'].astype(int)

data = data.sort_values('temp_price')
data = data.drop(columns=['temp_price'])

print(data)