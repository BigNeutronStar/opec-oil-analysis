import pandas as pd
import matplotlib.pyplot as plt


#### УЗНАТЬ ЧЕ ТАКОЕ КТАГЕОРИЗИРОВАННАЯ ДИАГРММА РАССЕИВАНИЯ И КАКИЕ АТРИБУТЫ НАМ БРАТЬ
df = pd.read_excel('./Work/Data/db.xlsx', sheet_name=0)

x = df['Цена за баррель']
y = df['Добыча (1000 баррелей)']

country_numbers = df['Номер страны по добыче'].unique()

plt.figure(figsize=(10, 6))
for country_number in country_numbers:
    subset = df[df['Номер страны по добыче'] == country_number]
    plt.scatter(subset['Цена за баррель'], subset['Добыча (1000 баррелей)'], label=country_number)
plt.title('Категоризированная диаграмма рассеивания:')
plt.xlabel('Цена за баррель')
plt.ylabel('Добыча (1000 баррелей/день) ')
plt.legend(title='Номер страны по добыче')
plt.grid(True)
plt.show()