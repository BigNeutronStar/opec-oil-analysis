import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Work/Data/nf_db.xlsx', sheet_name=0)

# Создаем новый столбец, содержащий информацию о номере страны в рейтинге и названии страны
df['Рейтинг и страна'] = df['Номер страны по добыче'].astype(str) + '. ' + df['Страна']

# Создание кластеризованной столбчатой диаграммы
plt.figure(figsize=(10, 6))
plt.bar(df['Рейтинг и страна'], df['Номер страны по добыче'])
plt.title('Кластеризованная столбчатая диаграмма')
plt.xlabel('Название страны')
plt.ylabel('Номер страны в рейтинге')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
