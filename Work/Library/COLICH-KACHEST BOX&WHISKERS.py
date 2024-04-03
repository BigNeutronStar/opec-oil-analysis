import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Work/Data/nf_db.xlsx', sheet_name=0)

# Построение категоризированной гистограммы box-and-whiskers (ящик с усами)
df.boxplot(by='Страна', column='Добыча (1000 баррелей/день)', grid=True)
plt.suptitle('')

df.boxplot(by='Номер страны по добыче', column='Добыча (1000 баррелей/день)', grid=True)
plt.suptitle('')

plt.show()