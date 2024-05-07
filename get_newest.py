import pandas as pd
from tabulate import tabulate

data = pd.read_csv('data.csv')

data = data.sort_values('year', ascending=False)
data = data.drop(columns=['date_of_publication'])

print(tabulate(data, headers='keys', tablefmt='rst'))