import numpy as np

import sys
sys.path.append('./Work/Library')

from dbmanager import *

bd['date_id'] = np.tile(np.arange(dates.size), countries.size)
bd['Дата'] = np.tile(dates.dt.strftime('%d.%m.%Y'), countries.size)
bd['Цена за баррель'] = np.tile(price, countries.size)
bd['Курс рубля'] = np.tile(currency, countries.size)


bd['country_id'] = np.repeat(np.arange(countries.size), dates.size)
bd['Страна'] = np.repeat(countries, dates.size)
bd['Номер страны по добыче'] = np.repeat(ratings, dates.size)

prod = []
for row in productions.values():
    prod = np.append(prod, np.repeat(row, dates_count))
bd['Среднедневная добыча за год (1000 бар/д)'] = prod

prod = []
for c in countries:
    prod = np.append(prod, daily_production[c])
bd['Добыча (1000 бар)'] = prod

bd.to_excel(path, index=False)

