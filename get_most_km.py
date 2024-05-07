import pandas as pd
from tabulate import tabulate

data = pd.read_csv('data.csv')


data['temp_driven_km'] = data['driven_km'].str.replace(' km', '')
data['temp_driven_km'] = data['temp_driven_km'].str.replace(' ', '')
data['temp_driven_km'] = data['temp_driven_km'].astype(int)

data = data.sort_values('temp_driven_km', ascending=False)
data = data.drop(columns=['temp_driven_km'])

print(tabulate(data, headers='keys', tablefmt='rst'))