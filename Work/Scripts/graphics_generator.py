import matplotlib.pyplot as plt
import numpy as np

from Library.databases import *

### box & whiskers
# currency.boxplot(column='Курс', grid=True, showmeans=True)
# plt.title('Курс 2006-2022 гг.')
# plt.ylabel('1$/1Р')
# plt.show()

# price.boxplot(column='Цена', grid=True, showmeans=True)
# plt.title('Цена на нефть 2006-2022 гг.')
# plt.ylabel('Рубли')
# plt.show()

# plt.figure(figsize=(10,6))
# positions = np.arange(2, len(countries) * 2 + 1, 2)

# plt.boxplot(production.values(), showmeans=True, positions=positions)
# plt.title('Среднедневная добыча 2006-2022 гг.')
# plt.xticks(positions, [c for c in countries], rotation = 15)
# plt.ylabel('Среднедневная добыча (1000 бар/д)')
# plt.grid()
# plt.suptitle('')
# plt.show()

####### считать дневную добычу из daily production для определенного года указанного и сделать график для нее в указанном году по странам
# year = years[0]

#### Графики измененения цены и курса
# plt.figure(figsize=(10,6))
# plt.plot(currency['Дата'], currency['Курс'], label='Курс рубля')
# plt.title('Курс 2006-2022 гг.')
# plt.xlabel('Дата')
# plt.ylabel('Рубли')
# plt.xticks(rotation=0)
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(10,6))
# plt.plot(price['Дата'], price['Цена'], label='Цена на нефть')
# plt.title('Цена на нефть 2006-2022 гг.')
# plt.xlabel('Дата')
# plt.ylabel('Рубли')
# plt.xticks(rotation=0)
# plt.grid(True)
# plt.show()

####### Кластеризованная столбчатая
# fig = plt.figure(figsize=(30, 6))
# ax = fig.add_subplot()
# ax.set_ylabel('Среднедневная добыча (1000 бар/д)')
# fig.suptitle("Кластеризованная столбчатая диаграмма по среднедневной добыче")
# x = years

# y1 = production["Congo"]
# y2 = production["Iraq"]
# y3 = production["Algeria"]
# y4 = production["Angola"]
# y5 = production["Equatorial Guinea"]
# y6 = production["Gabon"]
# y7 = production["IR Iran"]
# y8 = production["Kuwait"]
# y9 = production["Libya"]
# y10 = production["Nigeria"]
# y12 = production["United Arab Emirates"]
# y13 = production["Venezuela"]
# bar_width = 0.05

# ax.bar([i - 6*bar_width for i in x], y1, width=bar_width, align='center', label="Congo")
# ax.bar([i - 5*bar_width for i in x], y2, width=bar_width, align='center', label="Iraq")
# ax.bar([i - 4*bar_width for i in x], y3, width=bar_width, align='center', label="Algeria")
# ax.bar([i - 3*bar_width for i in x], y4, width=bar_width, align='center', label="Angola")
# ax.bar([i - 2*bar_width for i in x], y5, width=bar_width, align='center', label="Equatorial Guinea")
# ax.bar([i - bar_width for i in x], y6, width=bar_width, align='center', label="Gabon")
# ax.bar([i for i in x], y7, width=bar_width, align='center', label="IR Iran")
# ax.bar([i + bar_width for i in x], y8, width=bar_width, align='center', label="Kuwait")
# ax.bar([i + 2*bar_width for i in x], y9, width=bar_width, align='center', label="Libya")
# ax.bar([i + 3*bar_width for i in x], y10, width=bar_width, align='center', label="Nigeria")
# ax.bar([i + 4*bar_width for i in x], y12, width=bar_width, align='center', label="United Arab Emirates")
# ax.bar([i + 5*bar_width for i in x], y13, width=bar_width, align='center', label="Venezuela")
# ax.set_xticks([i for i in x])
# ax.set_xticklabels(x, rotation=45, ha='right', fontsize=10)
# plt.grid(True, axis='y')
# plt.legend(loc='upper right', bbox_to_anchor=(1.13, 1))
# plt.show()


###### Категоризированная гистограмма

# fig, axs = plt.subplots(1, len(years))
# plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)

# for i in range(len(years)):
#     data = np.array([prd[i] for prd in productions.values()])
# plt.show()
prd = [prod[0] for prod in production.values()]
plt.hist(prd)
plt.show()

