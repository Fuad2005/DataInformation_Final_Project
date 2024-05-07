from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')

data['temp_price'] = data['price'].str.replace(' AZN', '')
data['temp_price'] = data['temp_price'].str.replace(' ', '')
data['temp_price'] = data['temp_price'].astype(int)

data['temp_driven_km'] = data['driven_km'].str.replace(' km', '')
data['temp_driven_km'] = data['temp_driven_km'].str.replace(' ', '')
data['temp_driven_km'] = data['temp_driven_km'].astype(int)

# Sort data by 'temp_driven_km'
data = data.sort_values('temp_driven_km')

plt.plot(data['temp_driven_km'], data['temp_price'])

plt.xlabel('Kilometers Driven')
plt.ylabel('Price')
plt.title('Price by Kilometers Driven')

plt.show()