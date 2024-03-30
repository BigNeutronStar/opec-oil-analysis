import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('./Work/Data/nf_db.xlsx', sheet_name=0)

grouped_data = df.groupby('Страна')['Номер страны по добыче'].mean()
plt.figure(figsize=(10, 6))
grouped_data.plot(kind='bar')
plt.title('Кластеризованная столбчатая диаграмма')
plt.xlabel('Название страны')
plt.ylabel('Номер страны в рейтинге')
plt.xticks(rotation=0)
plt.yticks(list(grouped_data))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
