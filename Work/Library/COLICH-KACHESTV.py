import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Work/Data/nf_db.xlsx', sheet_name=0)

grouped_data1 = df.groupby('Страна')['Средняя добыча за год (1000 баррелей/день)'].mean()
grouped_data2 = df.groupby('Номер страны по добыче')['Средняя добыча за год (1000 баррелей/день)'].mean()
# Построение категоризированной гистограммы
plt.figure(figsize=(10, 6))
grouped_data1.plot(kind='bar')
plt.title('Среднегодовая добыча нефти по странам')
plt.xlabel('Страна')
plt.ylabel('Средняя добыча нефти (1000 баррелей/день)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.figure(figsize=(10, 6))
grouped_data2.plot(kind='bar')
plt.title('Среднегодовая добыча нефти по странам')
plt.xlabel('Номер страны по добыче')
plt.ylabel('Средняя добыча нефти (1000 баррелей/день)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
