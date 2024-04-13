import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Work/Data/nf_db.xlsx', sheet_name=0)
currency_pair = pd.read_excel('./Work/Data/currency-pair_db.xlsx')
oil_price = pd.read_excel('./Work/Data/oil-price_db.xlsx')

oil_prod_country = df.groupby('Страна')['Добыча (1000 баррелей)'].mean()
oil_prod_number = df.groupby('Номер страны по добыче')['Добыча (1000 баррелей)'].mean()

currency_pair['Date'] = pd.to_datetime(currency_pair['Date'], format='%m.%d.%Y')
currency_pair.sort_values(by='Date', inplace=True)

plt.bar(currency_pair['Date'], currency_pair['Course'])
plt.title('Курс доллара к рублю')
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

oil_price['Date'] = pd.to_datetime(oil_price['Date'], format='%Y-%m-%d')
oil_price.sort_values(by='Date', inplace=True)

plt.bar(oil_price['Date'], oil_price['Price'])
plt.title('Цена на нефть')
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

oil_prod_country.plot(kind='bar')
plt.title('Среднедневная добыча нефти по странам')
plt.xlabel('Страна')
plt.ylabel('Средняя добыча в день (1000 бареллей)')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()
