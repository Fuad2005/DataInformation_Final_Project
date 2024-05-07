from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')

data['temp_price'] = data['price'].str.replace(' AZN', '')
data['temp_price'] = data['temp_price'].str.replace(' ', '')
data['temp_price'] = data['temp_price'].astype(int)

# Calculate average price for each year
average_price_per_year = data.groupby('year')['temp_price'].mean()

# Create line graph
plt.plot(average_price_per_year.index, average_price_per_year.values)

plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Price vs Year')

plt.show()