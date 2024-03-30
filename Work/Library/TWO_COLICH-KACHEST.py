import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Work/Data/nf_db.xlsx', sheet_name=0)

x = df['Цена за баррель']
y = df['Средняя добыча за год (1000 баррелей/день)']

country_numbers = df['Номер страны по добыче'].unique()

plt.figure(figsize=(10, 6))
for country_number in country_numbers:
    subset = df[df['Номер страны по добыче'] == country_number]
    plt.scatter(subset['Цена за баррель'], subset['Средняя добыча за год (1000 баррелей/день)'], label=country_number)
plt.title('Категоризированная диаграмма рассеивания:')
plt.xlabel('Цена за баррель')
plt.ylabel('Средняя добыча за год (1000 баррелей/день)')
plt.legend(title='Номер страны по добыче')
plt.grid(True)
plt.show()