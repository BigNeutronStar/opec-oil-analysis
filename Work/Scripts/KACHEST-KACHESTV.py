import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Work/Data/nf_db.xlsx', sheet_name=0)


# узнать че такое кластеризованная столб диаграма и сделать из базы данных rating для каждой страны
grouped_data = df.groupby('Страна')['Номер страны по добыче'].mean()
grouped_data.plot(kind='bar', width=0.1)
plt.title('Кластеризованная столбчатая диаграмма')
plt.xlabel('Название страны')
plt.ylabel('Номер страны в рейтинге')
plt.xticks(rotation=0)
plt.yticks(list(grouped_data))
plt.grid(True)
plt.show()
