import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Work\\Data\\nf_db.xlsx', sheet_name=None)['1 нф']

# Построение категоризированной гистограммы box-and-whiskers (ящик с усами)
df.boxplot(by='Страна', column='Средняя добыча за год (1000 баррелей/день)', grid=False)
plt.show()