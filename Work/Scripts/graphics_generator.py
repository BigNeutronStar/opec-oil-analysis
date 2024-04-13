import matplotlib.pyplot as plt
import numpy as np

from Library.databases import *

currency.boxplot(column='Курс', grid=True, showmeans=True)
plt.ylabel('1$/1Р')
plt.show()

price.boxplot(column='Цена', grid=True, showmeans=True)
plt.ylabel('Рубли')
plt.show()

country = "Algeria"

####### сдеать для средневной добычи по всем годам

plt.boxplot(production[country], showmeans=True, labels=('Среднедневная доыбча', country))
plt.grid()
plt.suptitle('')
plt.ylabel('Среднедневная добыча')
plt.show()

####### считать дневную добычу из daily production для определенного года указанного и сделать график для нее в указанном году по странам






# fig, axs = plt.subplots(1, len(years))
# plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)

# for i in range(len(years)):
#     data = np.array([prd[i] for prd in productions.values()])

# plt.show()