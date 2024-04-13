import os
from openpyxl import Workbook
from Library import databases
from Library.paths import output_dir, output_paths, public_paths

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    for path in output_paths.values():
        print(path)
        Workbook().save(path)

databases.read(public_paths)
databases.form_date(output_paths['date'])
databases.form_rating(output_paths['rating'])
databases.form_dailyproduction(output_paths['dailyprd'])





























# bd['date_id'] = np.tile(np.arange(dates.size), countries.size)
# bd['Дата'] = np.tile(dates.dt.strftime('%d.%m.%Y'), countries.size)
# bd['Цена за баррель'] = np.tile(price, countries.size)
# bd['Курс рубля'] = np.tile(currency, countries.size)


# bd['country_id'] = np.repeat(np.arange(countries.size), dates.size)
# bd['Страна'] = np.repeat(countries, dates.size)
# bd['Номер страны по добыче'] = np.repeat(ratings, dates.size)

# prod = []
# for row in productions.values():
#     prod = np.append(prod, np.repeat(row, dates_count))
# bd['Среднедневная добыча за год (1000 бар/д)'] = prod

# prod = []
# for c in countries:
#     prod = np.append(prod, daily_production[c])
# bd['Добыча (1000 бар)'] = prod

# bd.to_excel(path, index=False)

