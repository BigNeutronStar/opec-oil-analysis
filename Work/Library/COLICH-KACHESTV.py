import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./Work/Data/nf_db.xlsx', sheet_name=0)
data_course = pd.read_excel('./Work/Data/курс рубля.xlsx')

country_dobych = df.groupby('Страна')['Средняя добыча за год (1000 баррелей/день)'].mean()
number_dobych = df.groupby('Номер страны по добыче')['Средняя добыча за год (1000 баррелей/день)'].mean()

data_course.plot(x='Date', y='Price', kind='line')

# Построение категоризированной гистограммы

# country_dobych.plot(kind='bar')
# plt.title('Среднегодовая добыча нефти по странам')
# plt.xlabel('Страна')
# plt.ylabel('Средняя добыча нефти (1000 баррелей/день)')
# plt.xticks(rotation=45)
# plt.grid(axis='y', linestyle='--', alpha=0.7)


# number_dobych.plot(kind='bar')
# plt.title('Среднегодовая добыча нефти по странам')
# plt.xlabel('Номер страны по добыче')
# plt.ylabel('Средняя добыча нефти (1000 баррелей/день)')
# plt.xticks(rotation=45)
# plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
