import pandas as pd
import matplotlib.pyplot as plt

dfs = pd.read_excel('Work\\Data\\nf_db.xlsx', sheet_name=None)

for i, df in dfs.items():
    grouped_data = df.groupby('Страна')['Средняя добыча за год (1000 баррелей/день)'].mean()

    # Построение категоризированной гистограммы
    plt.figure(figsize=(10, 6))
    grouped_data.plot(kind='bar', color='skyblue')
    plt.title('Среднегодовая добыча нефти по странам')
    plt.xlabel('Страна')
    plt.ylabel('Средняя добыча нефти (1000 баррелей/день)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()