from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')

data['temp_price'] = data['price'].str.replace(' AZN', '')
data['temp_price'] = data['temp_price'].str.replace(' ', '')
data['temp_price'] = data['temp_price'].astype(int)

# Modify bins
bins = [0, 50000, 100000, 200000]

plt.figure(figsize=(4, 4))
plt.hist(data['temp_price'], bins=bins, edgecolor='black')

# Modify bin names
bin_names = ['0-50k', '50k-100k', '100k+']
plt.xticks([0, 50000, 100000], bin_names)

plt.xlabel('Price Range')
plt.ylabel('Number of Cars')
plt.title('Distribution of Cars by Price Range')

plt.show()